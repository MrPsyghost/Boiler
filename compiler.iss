#define MyAppName "Boiler"
#define MyAppVersion "0.0.1"
#define MyAppPublisher "MrPsyghost"
#define MyAppURL "https://mrpsyghost.onrender.com/"
#define MyAppExeName "boiler.exe"

[Setup]
AppId={{F18A38E8-9691-406A-860B-0650615BE53A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

PrivilegesRequired=admin
ChangesEnvironment=yes

AllowNoIcons=yes
OutputDir=C:\Users\shiva\OneDrive\Desktop\Boiler\dist
OutputBaseFilename=boiler-setup-v0.0.1-beta
SetupIconFile=C:\Users\shiva\OneDrive\Desktop\Boiler\src\boiler.ico

SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\shiva\OneDrive\Desktop\Boiler\dist\boiler.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\shiva\OneDrive\Desktop\Boiler\dist\boiler.cfg"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Registry]
; Add Boiler's installation directory to the system PATH.
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath(ExpandConstant('{app}')); Flags: preservestringtype

[Code]

function NeedsAddPath(Param: string): Boolean;
var
  ExistingPath: string;
  NormalizedPath: string;
begin
  if not RegQueryStringValue(
    HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    ExistingPath
  ) then
    ExistingPath := '';

  NormalizedPath := ';' + Uppercase(ExistingPath) + ';';
  Result := Pos(';' + Uppercase(Param) + ';', NormalizedPath) = 0;
end;

procedure RemoveBoilerFromPath();
var
  ExistingPath: string;
  NewPath: string;
  Entry: string;
  StartPos: Integer;
  EndPos: Integer;
  AppPath: string;
begin
  if not RegQueryStringValue(
    HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    ExistingPath
  ) then
    Exit;

  AppPath := RemoveBackslash(ExpandConstant('{app}'));
  NewPath := '';
  StartPos := 1;

  while StartPos <= Length(ExistingPath) do
  begin
    EndPos := StartPos;

    while (EndPos <= Length(ExistingPath)) and
      (ExistingPath[EndPos] <> ';') do
      EndPos := EndPos + 1;

    Entry := Copy(ExistingPath, StartPos, EndPos - StartPos);

    if CompareText(RemoveBackslash(Trim(Entry)), AppPath) <> 0 then
    begin
      if NewPath <> '' then
        NewPath := NewPath + ';';

      NewPath := NewPath + Entry;
    end;

    StartPos := EndPos + 1;
  end;

  RegWriteExpandStringValue(
    HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    NewPath
  );
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usUninstall then
    RemoveBoilerFromPath();
end;