# How to quick create .gitignore in right menu

This article describes how to add a quick way to create a .gitignore file in the folder right-click menu.

We have two ways to create it, one is to add a new menu in the folder right-click menu, make it to create a .gitignore file immediately after being clicked.

![create-.gitignore-file-in-right-menu](./clip_20220702_014510.png)

The second way is to add the .gitignore file to the folder's New menu.

![create-.gitignore-file-in-new-menu](./clip_20220702_012737.png)

## Add a command to create .gitignore in right menu

> **Note** windows 8.1 system does not allow the direct creation of files starting with ".", this OS can only use this way.

First of all, we know that running the following command directly can create a .gitignore file this current folder and write "*" as the content to it.

```cmd
echo *>.gitignore
```

So all we have to do is, add this line of command to the context menu.

To do this, we follow the steps below:

1. Open regedit, create a key in

    ```reg
    HKEY_CLASSES_ROOT\Directory\Background\shell
    ```

    and name it `gitcreateignore` or other name you like.

1. Create a subkey under the key you just created, name it `command`.

1. Set the (default) value to:

    ```cmd
    cmd /c echo *>.gitignore
    ```

    ![regedit command](./clip_20220702_014427.png)

1. Ok, let's do a test. Right click in any folder background, you should see the menu like:

    ![right menu](./clip_20220702_014510.png)

1. Click it, then there should be a .gitignore file with the content * created in this folder.

<!-- Here I also provide a way to put it into submenu.

![sub menu](./clip_20220622_043009.png)

![right menu](./clip_20220622_043052.png) -->

## Add .gitignore type file in folder new menu

> **Note** I used the environment registered in the registry after vscode installation.

1. Goto `HKEY_CLASSES_ROOT\.gitignore` and set the (default) value to `VSCode.gitignore`.

    ![key .gitignore](./clip_20220702_013943.png)

1. Create a `ShellNew` key.

1. Create a `FileName` string value, and set it to `..gitignore`.

    ![key ShellNew](./clip_20220702_013909.png)

1. Open C:\\Windows\\ShellNew, Create a new "..gitignore" file by your self.

    And you can also add any content in it, like '*', or '#' etc.

1. Right click any folder, select new menu, you should see like:

    ![right menu](./clip_20220702_012737.png)

    Click it, OS will create a "New Git Ignore Source File.gitignore" file, and the content of the file should be the same as C:\\Windows\\ShellNew\\..gitignore.
