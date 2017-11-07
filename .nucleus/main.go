package main

import (
    "fmt"
    "os"
)

// Setup settings vars

var SET_BIN = true
var SET_VENV = false
var SET_CACHE = false
var SET_DATA = false
var SET_HISTORY = false
var SET_DB = false

type NLS_settings struct {
    kind string
    name string
    cmd []string
    db_cred [string] // "{db}:host:port:user:pw"
                     // ""
}

NLS_BIN = NLS_settings{kind: "dir",
                       name: "bin"}
NLS_VENV = NLS_settings{kind: "cmd",
                        name: "venv",
                        cmd: "cd $NUCLEUS && goenv nvenv"}
NLS_CACHE = NLS_settings{kind: "dir",
                         name: "cache"}
NLS_DATA = NLS_settings{kind: "dir",
                        name: "data"}
NLS_HISTORY = NLS_settings{kind: "file",
                           name: "history"}
NLS_DB = NLS_settings{kind: "db",
                      name: "Nucleus_DB",
                      db_cred: "mysql:localhost:3306:root:uehMLMRw"}

func isError(err error) bool {
	if err != nil {
		fmt.Println(err.Error())
	}
	return (err != nil)
}

func CreateDirectory(dir string) (status bool){
    _, err := os.Stat(dir)
    if os.IsNotExist(err) {
        os.Mkdir(dir, os.ModePerm)
        return true
    } else {
        return false
    }
}

func CreateFile(path string) (status bool) {
	var _, err = os.Stat(path)
	// create file if not exists
	if os.IsNotExist(err) {
		var file, err = os.Create(path)
		if isError(err) {
            return false
        } else {
            return true
        }
		defer file.Close()
	} else {
        return false
    }
    return false
}

func ExecOsCmds() {

}

type Dotfiles struct {
    // Dotfiles struct holding Dotfiles et their settings directory
    setup bool
    directory string
    settings_directory string
}

func (df *Dotfiles) Check() bool {
    // Checks Dotfiles dir exists
    return ! (os.Getenv("DOTFILES") == "")
}

func (df *Dotfiles) initialize() bool {
    // Initialize Dotfiles struct with DOTFILES real data
    if df.Check() {
        df.directory = os.Getenv("DOTFILES")
        df.settings_directory = os.Getenv("DF_SETTINGS")
        df.setup = true
        return true
    } else {
        return false
    }
}

type Nucleus struct {
    // Nucleus Structure
    dotfiles Dotfiles
    directory string
    set_bin bool
    set_venv bool
    set_cache bool
    set_data bool
    set_history bool
    set_db bool
}

func (nucleus *Nucleus) initialize() bool {
    //
    init_status := nucleus.dotfiles.initialize()
    if init_status {
        nucleus.directory = os.Getenv("NUCLEUS")
        nucleus.set_bin = SET_BIN
        return true
    } else {
        return false
    }
}

func (nucleus *Nucleus) ShowConfiguration() {
    fmt.Println("-------- Nucleus Configuration ---------")
    fmt.Println("Nucleus Directory :", nucleus.directory)
    fmt.Println("          SET_BIN :", nucleus.set_bin)
    fmt.Println("         SET_VENV :", nucleus.set_venv)
    fmt.Println("        SET_CACHE :", nucleus.set_cache)
    fmt.Println("         SET_DATA :", nucleus.set_data)
    fmt.Println("      SET_HISTORY :", nucleus.set_history)
    fmt.Println("     SET_DATABASE :", nucleus.set_db)
    fmt.Println("-----------------------------------------")
}

func (nucleus *Nucleus) MakeNucleusDirRoot() {
    if CreateDirectory(nucleus.directory) {
        fmt.Println("[ OK ] .. Created Nucleus Root directory")
    } else {
        fmt.Println("[WARN] ... Nucleus root directory exists already")
    }
}

func (nucleus *Nucleus) MakeSettings(directory bool, file bool,
    command bool, entry ...string) {
    if directory {
        dir_name := nucleus.directory + "/" + entry[0]
        if CreateDirectory(dir_name) {
            fmt.Println("[ OK ] ... Created", dir_name)
        } else {
            fmt.Println("[WARN] ...", dir_name, "already exists")
        }
    } else if file {
        file_name := nucleus.directory + "/" + entry[0]
        if CreateFile(file_name) {
            fmt.Println("[ OK ] ... Created", file_name)
        } else {
            fmt.Println("[WARN] ...", file_name, "already exists")
        }
    } else if command {
        fmt.Println("")
    }
}

func SetupNucleus() bool {
    n := Nucleus{}
    is := n.initialize()
    if is {
        n.ShowConfiguration()
        n.MakeNucleusDirRoot()
        n.MakeSettings(false, true, true, "loul")
    } else {
        fmt.Println("noobs")
    }
    return true
}

func main() {
    fmt.Println(SetupNucleus())
}
