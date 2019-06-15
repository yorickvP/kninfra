{ pkgs, lib, config }:
{
  environment.systemPackages = with pkgs; [
    git
    htop
    iotop
    ncdu
    (vim_configurable.customize {
      customRC = builtins.readFile ../salt/states/common/virc;
    })
    python36Packages.ipython
    python36Packages.python
    psmisc
    socat
    mutt
  ];
  i18n.supportedLocales = [ "en_US.UTF-8/UTF-8" "nl_NL.UTF-8/UTF-8" ];
  services.logcheck = {
    enable = true;
    extraRulesDirs = [ (builtins.fetchGit {
      url = https://github.com/bwesterb/x-logcheck;
    }) ];
  };
  # TODO: postfix?
  # TODO: motd (rest)
  users.motd = ''
     ___   _____   __  __ __                    _  __     __   __   
    / _ | / __/ | / / / //_/__ ________  ___   / |/ /__  / /__/ /____ __ _ 
   / __ |_\ \ | |/ / / ,< / _ `/ __/ _ \/ -_) /    / _ \/  '_/ __/ -_)  ' \
  /_/ |_/___/ |___/ /_/|_|\_,_/_/ / .__/\__/ /_/|_/\___/_/\_\\__/\__/_/_/_/
  '';
  config.services.sshguard = {
    enable = true;
    whitelist = [
      "127.0.0.0/8" "10.0.0.0/24"
      "37.251.64.47/32" "82.93.241.107/32"
      "82.94.240.40/32" "37.252.124.223/32"
      "sw.w-nz.com" "62.163.41.99/32"
    ];
  };
}
