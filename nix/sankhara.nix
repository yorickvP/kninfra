{ config, pkgs, lib }:
let
kninfra = pkgs.python36Packages.buildPythonApplication {
  name = "kninfra";
  src = pkgs.fetchgit {
    url = https://github.com/karpenoktem/kninfra;
    rev = "a6b3b9059c7746851d41bf6b927862fe82217deb";
    sha256sum = "";
  };
  buildInputs = with python36Packages; [
    django msgpack pyparsing markdown
    pymongo pillow html2text httplib2
    pyx unidecode
    # mirte sarah uwsgi tarjan reserved
    pymysql iso8601 google_api_python_client
    # zipseeker pyldap
    # sdnotify
    pyasn1

            # python2 packages for hans
            - python-six
            - python-django
            - python-pymongo

            # prerquisites for pyldap
            - libsasl2-dev
            - libldap2-dev
            - libssl-dev
  ];
};
whimd = name: {
  Type = "notify";
  ExecStart = "${kninfra}/bin/${name}";
  RuntimeDirectory = name;
  SupplementaryGroups = "infra";
};
tunnel = name: {
  ExecStart = "${kninfra}/bin/${name}-tunnel";
  RuntimeDirectory = name;
  SupplementaryGroups = "infra";
};
in
{
  users.groups.extraGroups.infra = {};
  services.mongodb.enable = true;
  services.uwsgi = {
    enable = true;
    instance = {
      type = "normal";
      pythonPackages = [ kninfra ];
      module = "kn.wsgi";
      cheap = true;
      env = "DJANGO_SETTINGS_MODULE=kn.settings";
      socket = "${config.services.uwsgi.runDir}/S-django";
    };
  };
  nginx.virtualHosts.kninfra = {
    locations."/".extraConfig = ''
      uwsgi_pass unix:${config.services.uwsgi.instance.socket}
      client_max_body_size 10M;
    '';
    locations."/djmedia".root = "${kninfra}/media";
  };
  systemd.services = {
    uswgi = rec {
      requires = [ "giedo.service" ];
      after = requires;
    };
    daan = rec {
      description = "Daan applies changes on phassa thought up by Giedo";
      wantedBy = [ "multi-user.target" ];
      requires = [ "mongodb.service" ];
      after = requires;
      ServiceConfig = whimd "daan";
    };
    hans = rec {
      description = "Hans handles Mailman for Giedo";
      wantedBy = [ "multi-user.target" ];
      ServiceConfig = whimd "hans";
    };
    giedo = rec {
      description = "Giedo figures out what to change";
      wantedBy = [ "multi-user.target" ];
      requires = [ "mongodb.service" "daan.service" "cilia-tunnel.service" "moniek-tunnel.service" "hans.service" ];
      after = requires;
      ServiceConfig = whimd "giedo";
    };
    cilia-tunnel = rec {
      description = "Links Cilia socket on phassa and sankhara";
      wantedBy = [ "multi-user.target" ];
      ServiceConfig = tunnel "cilia";
    };
    moniek-tunnel = rec {
      description = "Links Moniek socket on phassa and sankhara";
      wantedBy = [ "multi-user.target" ];
      ServiceConfig = tunnel "moniek";
    };
  };

}
