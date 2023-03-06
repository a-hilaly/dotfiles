DOTFILES_PATH="~/source/github.com/a-hilaly/dotfiles"

install:
	@echo installing dotfiles - all
	echo "source $(DOTFILES_PATH)/activate" >> ~/.bash_profile

install-min:
	@echo installing dotfiles - min
	echo "source $(DOTFILES_PATH)/activate-min" >> ~/.bash_profile
	
───────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ {
   2   │     "go.buildTags": "codegen",
   3   │     "go.buildOnSave": "package",
   4   │     "go.lintTool": "golint"
   5   │ }
