nfs packages:
    pkg.installed:
        - pkgs:
            - nfs-common
/mnt/phassa:
    mount.mounted:
        - device: {{ pillar['ip-phassa'] }}:/srv/nfs
        - fstype: nfs
        - mkmnt: true
        - opts: [ro]
