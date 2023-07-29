detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        "Ubuntu")
            install_linux
            ;;
        *)
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}
install_linux(){
    sudo echo "sudo python $HOME/.jsontrans/main.py \$1 \$2 \$3 \$4 \$5" > $HOME/.local/bin/jsontrans
    sudo echo 'echo "[*] Uninstalling jsontrans..." && sudo rm -rf $HOME/.jsontrans && sudo rm -rf $HOME/.local/bin/jsontrans && sudo rm -rf $HOME/.local/bin/jsontrans-uninstaller && echo "[*] jsontrans uninstall task done"' > $HOME/.local/bin/jsontrans-uninstaller
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.jsontrans"
    sudo chmod +x $HOME/.local/bin/jsontrans
    sudo chmod +x $HOME/.local/bin/jsontrans-uninstaller
}
install_termux(){
    cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.jsontrans"
    echo "python $HOME/.jsontrans/main.py \$1 \$2 \$3 \$4 \$5" > $PREFIX/bin/jsontrans
    echo 'echo "[*] Uninstalling jsontrans..." && rm -rf $HOME/.jsontrans && rm -rf $PREFIX/bin/jsontrans && rm -rf $PREFIX/bin/jsontrans-unisntaller && echo "[*] jsontrans uninstall task done"' > $PREFIX/bin/jsontrans-uninstaller
    chmod +x $PREFIX/bin/jsontrans
    chmod +x $PREFIX/bin/jsontrans-uninstaller
}
detect_platform