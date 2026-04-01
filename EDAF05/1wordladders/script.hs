{-# LANGUAGE TupleSections #-}
import Text.Read (readMaybe, Lexeme (String))
import qualified Data.Set as Set
import Data.Sequence (Seq, (|>), (<|))
import qualified Data.Sequence as Seq
import qualified Data.Map as Map
import Data.Maybe
import Control.Concurrent.STM (check)


import Distribution.Compat.CharParsing (CharParsing(string))
import Data.Foldable (for_)
import Text.Printf (FieldFormat(fmtChar))
import Data.List((\\), foldl')

type Visited = Set.Set String
type Graph = Map.Map String [String]
type Queue = Seq (String, Int)

-- Huvudfunktionen som läser in input, skapar grafen och utför BFS för varje query.
main :: IO ()
main = do
    input <- getContents
    let ls = lines input                 
        numbers = parseNumbers (head ls)
        restLines = tail ls
        words = parseWords restLines (head numbers)
        paths = parsePaths restLines (head numbers)
        graph = createGraph words
    for_ paths $ \p -> putStrLn $ bfsTest graph p

-- Tar ut de två talen som skickas med i inputen.
parseNumbers :: String -> [Int]
parseNumbers s = [n | w <- words s, Just n <- [readMaybe w :: Maybe Int]]

-- Skapar en lista av queries där varje query är en tuple av start och mål.
parsePaths :: [String] -> Int -> [(String, String)]
parsePaths xs y =
    let brute = drop y xs
    in  [(n,m) | w <- brute, (n,m) <- [(head (words w), words w !! 1)]]

-- Skapar en lista av ord som kommer bli noder i grafen.
parseWords :: [String] -> Int -> [String]
parseWords xs y = take y xs

-- Kollar om de sista n-1 bokstäverna i s1 finns i s2.
checkPath :: String -> String -> Bool
checkPath s1 s2 = null (drop 1 s1 \\ s2)

-- Skapar en graf där varje ord är en nod och det finns en kant mellan två noder om de skiljer sig på exakt en bokstav.
-- Grafen representeras som en Map där nyckeln är ett ord och värdet är en lista av närliggande ord.
createGraph :: [String] -> Graph
createGraph xs = Map.fromList [(x, [y | y <- xs, y /= x, checkPath x y]) | x <- xs]



-- BFS som använder en sequence som kö för att hålla reda på vilka noder som ska besökas. 
-- Set för att hålla reda på redan besökta noder. 
bfsTest :: Graph -> (String, String) -> String
bfsTest graph (start, goal) 
    | start == goal = "0"
    | otherwise = bfsHelperTest (Set.singleton start) (Seq.singleton (start, 0))
    where
        bfsHelperTest :: Visited -> Queue -> String
        bfsHelperTest visited queue = 
            case Seq.viewl queue of
                Seq.EmptyL -> "Impossible"
                (node, dist) Seq.:< q -> --pop
                    if node == goal
                        then show dist
                        else
                            let neighbors = Map.findWithDefault [] node graph
                                newNodes = filter (\n -> not (Set.member n visited)) neighbors  --if neighbor not in visited
                                newVisited = foldl' (flip Set.insert) visited newNodes
                                newQueue = q Seq.>< Seq.fromList (map (, dist + 1) newNodes) -- dist ++1 och motsvarande q ++ nextQueueItems, där nextQueueItems är "Seq.fromList (map (, dist + 1) newNodes"
                            in bfsHelperTest newVisited newQueue

{-
FÖLJANDE GJORDE ATT VI GICK FÅRN 9 MIN TILL MINDRE ÄN 2 MIN.
Stoppade i laddaren
Ändrade inställningar från energisparläge till hög prestanda
220 sekunder med ghc script.hs
108 sekunder med ghc -O2 script.hs

KODÄNDRINGAR:
Kompilatorn kan ha svårt att optimera föjande, vilket skapar en thunk:
    nextQueueItems = fmap (, dist + 1) (Seq.fromList newNodes) -- dist ++1
    newQueue = q Seq.>< nextQueueItems -- q ++ nextQueueItems


    newVisited = foldr Set.insert visited newNodes 
    BYTTES UT MOT:
    foldl' (flip Set.insert) visited newNodes
-}