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


--    TESTER   --
-- >>> checkPath "aaaaa" "aaaba"
-- True
-- >>> checkPath "aaaaa" "aaabb"
-- False
-- >>> checkPath "abcde" "abfge"
-- False


main :: IO ()
main = do
    input <- getContents
    let ls = lines input                 
        numbers = parseNumbers (head ls)
        restLines = tail ls
        words = parseWords restLines (head numbers)
        paths = parsePaths restLines (head numbers)
        graph = createGraph words
    -- showResult (fmap (pathToInt . bfs graph) paths)
    for_ paths $ \p -> putStrLn $ bfsTest graph p

parseNumbers :: String -> [Int]
parseNumbers s = [n | w <- words s, Just n <- [readMaybe w :: Maybe Int]]

parsePaths :: [String] -> Int -> [(String, String)]
parsePaths xs y =
    let brute = drop y xs
    in  [(n,m) | w <- brute, (n,m) <- [(head (words w), words w !! 1)]]

parseWords :: [String] -> Int -> [String]
parseWords xs y = take y xs



-- "\\" (listdifferens): Denna operator går igenom den vänstra listan och försöker ta bort motsvarande element från den högra
-- listan. Om det inte finns något motsvarande element i den högra listan så behålls elementet i den vänstra listan.
checkPath :: String -> String -> Bool
checkPath s1 s2 = null (drop 1 s1 \\ s2)


createGraph :: [String] -> Graph
createGraph xs = Map.fromList [(x, [y | y <- xs, y /= x, checkPath x y]) | x <- xs]


popSeq :: Seq a -> Maybe (a, Seq a)
popSeq q =
    case Seq.viewl q of
        Seq.EmptyL   -> Nothing
        x Seq.:< q'  -> Just (x, q')

neighbors :: Graph -> String -> [String]
neighbors graph node = Map.findWithDefault [] node graph

addToQueue :: (Queue, Visited) -> [String] -> (Queue, Visited)
addToQueue (queue, visited)
  = foldl
      (\ (q, v) n
         -> if Set.member n visited then
                (q, v)
            else
                (q Seq.|> n, Set.insert n v))
      (queue, visited)

graph = createGraph ["abcde", "bcdef", "cdefg", "defhg", "efghi"]
paths = [("abcde", "efghi"),("abcde", "cdefg"), ("abcde", "kkkkk")]
path2 = ("abcde", "efghi")

results = fmap (pathToInt . bfs graph) paths


showResult :: [Int] -> IO ()
showResult res = for_ res $ \x -> putStrLn (if x < 0 then "Impossible" else show x)

test :: IO() 
test = do showResult results

pathToInt :: Path -> Int
pathToInt x = length x - 1

bfs :: Graph -> (String, String) -> Path
bfs graph (start, goal) =
    let
        q :: Queue
        q = Seq.Empty |> start

        v :: Visited
        v = Set.insert start Set.empty

        p :: Path
        p = []

        st :: State
        st = (v,q,p)
    in
        bfsHelper st graph goal

bfsHelper :: State -> Graph -> String -> Path
bfsHelper (visited, queue, path) graph goal =
    if null queue
        then []
    else
        let
            (node, q) = case popSeq queue of
                Nothing -> ("", Seq.Empty)
                Just (node, q) -> (node, q)
            p = node : path
        in
            if node == goal
                then p
            else
                let
                    n = neighbors graph node
                    (q', v) = addToQueue (q, visited) n
                in
                    bfsHelper (v,q',p) graph goal

bfsTest :: Graph -> (String, String) -> String
bfsTest graph (start, goal) 
    | start == goal = "0"
    | otherwise = bfsHelperTest (Set.singleton start) (Seq.singleton (start, 0))
    where
        bfsHelperTest :: Visited -> QueueTest -> String
        bfsHelperTest visited queue = 
            case Seq.viewl queue of
                Seq.EmptyL -> "Impossible"
                (node, dist) Seq.:< q ->
                    if node == goal
                        then show dist
                        else
                            let neighbors = Map.findWithDefault [] node graph
                                newNodes = filter (\n -> not (Set.member n visited)) neighbors  
                                newVisited = foldr Set.insert visited newNodes
                                nextQueueItems = fmap (, dist + 1) (Seq.fromList newNodes)  -- Här ser vi till att path är given för varje nod. Lager 1, lager 2 osv. 
                                newQueue = q Seq.>< nextQueueItems
                            in bfsHelperTest newVisited newQueue





{- 
Fixat checkPath, createGraph, bfsTest och bfsHelperTest.
-}
