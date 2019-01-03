DOTFILES_PATH="~/Github/dotfiles"

install:
	@echo installing dotfiles - all
	echo "source $(DOTFILES_PATH)/activate" >> ~/.bash_profile

install-min:
	@echo installing dotfiles - min
	echo "source $(DOTFILES_PATH)/activate-min" >> ~/.bash_profile