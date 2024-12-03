class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        path = path.split("/")
        
        for p in path: 
            if dirs and p == "..":  ## removes parent directory
                dirs.pop()
            elif p not in [".", "..", ""]:
                dirs.append(p) ## add directory
        
        return "/" + "/".join(dirs)
