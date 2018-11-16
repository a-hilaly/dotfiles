DOTFILES_PATH="~/Github/dotfiles"

install:
	@echo installing dotfiles 
	echo "source $(DOTFILES_PATH)/activate" >> ~/.bash_profile