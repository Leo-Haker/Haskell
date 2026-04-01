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
import Data.List((\\))

type Visited = Set.Set String
type Queue = Seq.Seq String
type Path = [String]
type State = (Visited, Queue, Path)
type Graph = Map.Map String [String]
type QueueTest = Seq (String, Int)

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

parseNumbers :: String -> [Int]
parseNumbers s = [n | w <- words s, Just n <- [readMaybe w :: Maybe Int]]

parsePaths :: [String] -> Int -> [(String, String)]
parsePaths xs y =
    let brute = drop y xs
    in  [(n,m) | w <- brute, (n,m) <- [(head (words w), words w !! 1)]]

parseWords :: [String] -> Int -> [String]
parseWords xs y = take y xs

checkPath :: String -> String -> Bool
checkPath s1 s2 = null (drop 1 s1 \\ s2)


createGraph :: [String] -> Graph
createGraph xs = Map.fromList [(x, [y | y <- xs, y /= x, checkPath x y]) | x <- xs]



-- 
bfsTest :: Graph -> (String, String) -> String
bfsTest graph (start, goal) 
    | start == goal = "0"
    | otherwise = bfsHelperTest (Set.singleton start) (Seq.singleton (start, 0))
    where
        bfsHelperTest :: Visited -> QueueTest -> String
        bfsHelperTest visited queue = 
            case Seq.viewl queue of
                Seq.EmptyL -> "Impossible"
                (node, dist) Seq.:< q -> --pop
                    if node == goal
                        then show dist
                        else
                            let neighbors = Map.findWithDefault [] node graph
                                newNodes = filter (\n -> not (Set.member n visited)) neighbors  --if neighbor not in visited
                                newVisited = foldr Set.insert visited newNodes
                                nextQueueItems = fmap (, dist + 1) (Seq.fromList newNodes) -- dist ++1
                                newQueue = q Seq.>< nextQueueItems -- q ++ nextQueueItems
                            in bfsHelperTest newVisited newQueue
