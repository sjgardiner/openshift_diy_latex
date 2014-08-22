# texlive.profile
# Used for installing TeXLive using the install-tl script in batch mode
# Note that all tildes (~) in this file will be replaced with the value
# of $HOME during installation (TeXLive does not automatically do this
# for some of these directories, so our installation script takes care
# of it)
selected_scheme scheme-custom
TEXDIR ~/app-root/data/TeXLive
TEXMFCONFIG ~/.texlive2014/texmf-config
TEXMFHOME ~/app-root/repo/texmf
TEXMFLOCAL ~/app-root/data/TeXLive/texmf-local
TEXMFSYSCONFIG ~/app-root/data/TeXLive/texmf-config
TEXMFSYSVAR ~/app-root/data/TeXLive/texmf-var
TEXMFVAR ~/.texlive2014/texmf-var
binary_x86_64-linux 1
collection-basic 1
collection-binextra 1
collection-fontutils 1
collection-formatsextra 1
collection-games 1
collection-genericextra 1
collection-genericrecommended 1
collection-langenglish 1
collection-latex 1
collection-latexextra 1
collection-latexrecommended 1
collection-luatex 1
collection-mathextra 1
collection-metapost 1
collection-pictures 1
collection-plainextra 1
collection-pstricks 1
collection-publishers 1
collection-science 1
in_place 0
option_adjustrepo 1
option_autobackup 1
option_backupdir tlpkg/backups
option_desktop_integration 0
option_doc 0
option_file_assocs 0
option_fmt 1
option_letter 1
option_menu_integration 1
option_path 0
option_post_code 1
option_src 0
option_sys_bin /usr/local/bin
option_sys_info /usr/local/share/info
option_sys_man /usr/local/share/man
option_w32_multi_user 0
option_write18_restricted 1
portable 0
