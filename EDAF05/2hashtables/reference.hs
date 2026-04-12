
-- Translation of reference.py -- 
import qualified Data.Map as Map
import System.IO    
import Data.IORef
import Text.Read (Lexeme(String))

emptyMap :: Map.Map k a
emptyMap = Map.empty

main = do
    counter <- newIORef 0
    let emptyMap = Map.empty
    loop counter emptyMap


loop :: IORef Int -> Map.Map String Int-> IO ()
loop counter hashMap = do
    eof <- isEOF -- kollar om stdIn är slut
    if eof
        then return ()
        else do
            i <- readIORef counter       -- läsa
            line <- getLine
            let word = strip line
            -- gör något
            loop counter hashMap

strip :: String -> String
strip string = reverse $ dropWhile(== ' ') $ reverse $ dropWhile(== ' ') string
