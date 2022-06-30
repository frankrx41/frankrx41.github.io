# How to disable win+L to lock PC in windows 11

1. Open regedit and goto

    ```reg
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
    ```

1. Set 'DisableLockWorkstation' value to '2'

    ![DisableLockWorkstation](./Clip_20220630_093805.png)

    > **Note** 1: enbale 2: disable

1. It should work immediately
