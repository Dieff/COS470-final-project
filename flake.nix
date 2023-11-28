{
  description = "My final project for COS 470.";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          packages = with pkgs; 
            [ 
              # using python 3.11
              python311 virtualenv 
              # our emulator of choice
              mgba 
              # final report written in typst
              typst typst-live typst-lsp typst-fmt 
            ] ++
            # python packages
            (with pkgs.python311Packages; 
              [ 
                pip 
                # for IDE
                autopep8 flake8
                ]
            );
        };
      });
    };
}
