# The module containing the django configuration
# this is enabled with kn.django.enable = true;
# it configures nginx, mongo and an uwsgi systemd service
{ config, lib, pkgs, ... }:
let
  cfg = config.kn.django;
  # generate a json file with configuration for uwsgi
  kn_env = {
    DJANGO_SETTINGS_MODULE = "kn.settings_env";
    KN_GIEDO_SOCKET = config.kn.giedo.socket;
    KN_SECRET_KEY = "CHANGE ME";
    KN_CHUCK_NORRIS_HIS_SECRET = "CHANGE ME";
    KN_MONIEK_SOCKET = config.kn.moniek.socket;
    KN_FIN_YAML_PATH = "/var/lib/knfin/fins.yaml";
    # GRPC_VERBOSITY="DEBUG";
    # GRPC_TRACE="tcp";
  };
  uswgi_conf = pkgs.writeText "uwsgi.json" (builtins.toJSON {
    uwsgi = {
      plugins = "python3";
      chdir = pkgs.kninfra;
      module = "kn.wsgi";
      master = true;
      enable_threads = true;
      env = [
        "PYTHONPATH=${pkgs.kninfra.PYTHONPATH}"
      ];
    };
  });
  # customize the uwsgi package to have python3 support
  uwsgi_pkg = pkgs.uwsgi.override { plugins = [ "python3" ]; };
in {
  # defining the kn.django config settings
  options.kn.django = with lib; {
    enable = mkEnableOption "KN website";
    socket = mkOption {
      default = "/run/infra/S-django";
      description = "The socket path to use for UWSGI";
      type = types.path;
    };
  };
  options.kn.moniek = with lib; {
    enable = mkEnableOption "KN Moniek";
    socket = mkOption {
      default = "/run/infra/moniek";
      description = "The socket path to use for Moniek";
      type = types.path;
    };
  };
  options.kn.giedo = with lib; {
    enable = mkEnableOption "KN Giedo";
    socket = mkOption {
      default = "/run/infra/giedo";
      description = "The socket path to use for Giedo";
      type = types.path;
    };
  };
  config = lib.mkIf cfg.enable {
    services = {
      # TODO: limit access to mongodb
      mongodb.enable = true;
      nginx = {
        enable = true;
        virtualHosts.kn = {
          locations."/djmedia/".alias = "${pkgs.kninfra}/media/";
          locations."/".extraConfig = ''
            include ${pkgs.nginx}/conf/uwsgi_params;
            uwsgi_pass unix:${config.kn.django.socket};
           '';
        };
      };
    };
    users.groups.infra = {};
    # socket activation
    systemd.sockets.giedo = {
      wantedBy = [ "sockets.target" ];
      listenStreams = [ config.kn.giedo.socket ];
      socketConfig = {
        SocketGroup = "infra";
        SocketMode = "0660";
      };
    };
    systemd.sockets.moniek = {
      wantedBy = [ "sockets.target" ];
      listenStreams = [ config.kn.moniek.socket ];
      socketConfig = {
        SocketGroup = "infra";
        SocketMode = "0660";
      };
    };
    systemd.services.moniek = {
      environment = kn_env // { HOME = "/var/lib/knfin"; };
      path = [ pkgs.gitMinimal ];
      serviceConfig = {
        ExecStart = "${pkgs.kninfra}/utils/moniek.py";
        DynamicUser = true;
        Restart = "on-failure";
        Type = "notify";
        NotifyAccess = "all";
        StateDirectory = "knfin";
        WorkingDirectory = "/var/lib/knfin";
      };
      preStart = ''
        if [ ! -f $HOME/database-initialized ]; then
          cp ${../../salt/states/phassa/fin37.yaml} $HOME/fin37.yaml
          cp ${../../salt/states/phassa/fin42.yaml} $HOME/fin42.yaml
          cp ${../../salt/states/phassa/fins.yaml} $HOME/fins.yaml
          cp ${../../salt/states/phassa/fin.gnucash} $HOME/fin.gnucash
          pushd $HOME
          git init --bare fin
          git clone fin fin.tmp
          cd fin.tmp
          cp ../fin.gnucash .
          git add fin.gnucash
          git commit -m 'initial'
          git push
          cd ..
          rm -rf fin.tmp
          touch database-initialized
          popd
        fi
      '';
    };
    systemd.services.giedo = rec {
      requires = [ "mongodb.service" "kn_initial_state.service" ];
      after = requires;
      environment = kn_env;
      serviceConfig = {
        ExecStart = "${pkgs.kninfra}/utils/giedo.py";
        DynamicUser = true;
        Restart = "on-failure";
        SupplementaryGroups = "infra";
        Type = "notify";
        NotifyAccess = "all";
      };
    };
    systemd.sockets.kndjango = {
      wantedBy = [ "sockets.target" ];
      listenStreams = [ config.kn.django.socket ];
      socketConfig = {
        SocketGroup = "nginx";
        SocketUser = "nginx";
        SocketMode = "0660";
      };
    };
    systemd.services.kndjango = rec {
      requires = [ "mongodb.service" "kn_initial_state.service" ];
      after = requires;
      environment = kn_env;
      serviceConfig = {
        ExecStart = "${uwsgi_pkg}/bin/uwsgi --json ${uswgi_conf}";
        # allocate a dynamic user for every run. maximum sandboxing
        DynamicUser = true;
        Restart = "on-failure";
        KillSignal = "SIGQUIT";
        SupplementaryGroups = "infra";
        # uwsgi is systemd-aware
        Type = "notify";
        NotifyAccess = "all";
      };
    };
    systemd.services.kn_initial_state = rec {
      requires = [ "mongodb.service" ];
      after = requires;
      serviceConfig = {
        StateDirectory = "kndjango";
        Type = "oneshot";
        RemainAfterExit = true;
      };
      script = ''
        # initialize the DB if this has not happened before
        # TODO: only in VM
        if [ ! -f /var/lib/kndjango/database-initialized ]; then
          ${pkgs.kninfra}/libexec/initializeDb.py
          touch /var/lib/kndjango/database-initialized
        fi
      '';
    };
  };
}