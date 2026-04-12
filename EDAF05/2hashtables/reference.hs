
-- Translation of reference.py -- 
import qualified Data.Map as Map
import System.IO    
import Data.IORef

emptyMap :: Map.Map k a
emptyMap = Map.empty

main = do
    counter <- newIORef 0
    hashMap <- loop counter Map.empty
    let
        (count, word) = maximum (zip (Map.elems hashMap)  (Map.keys hashMap))
        possibleWords = Map.keys $ Map.filterWithKey(\k v -> v == count &&  k < word) hashMap
        word' = if null possibleWords then word else minimum possibleWords
    print(word, count)

loop :: IORef Int -> Map.Map String Int-> IO (Map.Map String Int)
loop counter hashMap = do
    eof <- isEOF -- kollar om stdIn är slut
    if eof
        then return hashMap
        else do
            i <- readIORef counter       -- läsa
            line <- getLine
            modifyIORef' counter (+1) 
            let word = strip line
                isPresent = Map.member word hashMap
                removeIt = (i `mod` 16) == 0
            if isPresent
                then if removeIt
                        then loop counter (Map.delete word hashMap)
                        else loop counter (Map.update addOne word hashMap)
                else if not removeIt 
                        then loop counter (Map.insert word 1 hashMap)
                        else loop counter hashMap

strip :: String -> String
strip string = reverse $ dropWhile(== ' ') $ reverse $ dropWhile(== ' ') string

addOne :: Num a => a -> Maybe a
addOne x = Just(x + 1)
