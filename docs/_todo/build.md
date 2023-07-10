# Build Binaries

We assume you want to build variant **alpha**.
**alpha** is a theoretical variant, the name of your variants might be different.

## Visual Studio Code

In the blue ribbon at the bottom (1) select a variant like _alpha_, (2) and the Kit _prod_ ,(3) choose the build target _elf_ and (4) click on build:
![vscode-build](img/vscode-build.png)

![vscode-build](img/build-binaries.gif)

## Command Line

The following shows the steps/commands when you use Windows PowerShell to do so.

```powershell
cd <Your root directory of repository>

.\build\spl-core\powershell\spl.ps1 -build -target link
```

## Binary Location

After the build all binaries can be found under `/build/{variant}`.


## Configuration

Configuration is done using KConfig. The target `Configuration` will open gui-config, a GUI tool to configure KConfig.
Within this configuration a variable expansion is possible for `string` configs:

* KConfig variables get replaced like: `${VARIABLE_NAME}`, e.g. `${SPL_RELEASE_VERSION}`
* environment variables get replaced with: `${ENV:VARIABLE_NAME}`, e.g. `${ENV:VARIANT}`  (VARIANT is exposed as environment variable, other internal variables as well)