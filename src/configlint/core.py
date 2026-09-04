from dataclasses import dataclass

@dataclass(frozen=True)
class Diagnostic:
    line:int
    message:str

def lint(text:str):
    out=[]; keys=set()
    for n,line in enumerate(text.splitlines(),1):
        s=line.strip()
        if not s or s.startswith('#'): continue
        if '=' not in s: out.append(Diagnostic(n,"missing '='")); continue
        key,value=s.split('=',1); key=key.strip()
        if not key: out.append(Diagnostic(n,"empty key"))
        if key in keys: out.append(Diagnostic(n,f"duplicate key: {key}"))
        keys.add(key)
        if not value.strip(): out.append(Diagnostic(n,f"empty value: {key}"))
    return out
