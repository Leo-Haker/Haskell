import Text.Read (readMaybe)
import qualified Data.Set as Set
import Data.Sequence (Seq, (|>), (<|))
import qualified Data.Sequence as Seq
import qualified Data.Map as Map
import Data.Maybe
import Control.Concurrent.STM (check)
import qualified Data.Binary.Builder as Seq
import Distribution.Compat.CharParsing (CharParsing(string))
import Data.Foldable (for_)

type Visited = Set.Set String
type Queue = Seq.Seq String
type Path = [String]
type State = (Visited, Queue, Path)
type Graph = Map.Map String [String]

main :: IO ()
main = do
    input <- getContents
    let ls = lines input                 -- dela upp input i rader
        numbers = parseNumbers (head ls) -- första raden → tal
        restLines = tail ls
        words = parseWords restLines (head numbers)
        paths = parsePaths restLines (head numbers)
        graph = createGraph words
        results = fmap (pathToInt . bfs graph) paths


        --  
    print numbers
    print words
    print paths

parseNumbers :: String -> [Int]
parseNumbers s = [n | w <- words s, Just n <- [readMaybe w :: Maybe Int]]

parsePaths :: [String] -> Int -> [(String, String)]
parsePaths xs y =
    let brute = drop y xs
    in  [(n,m) | w <- brute, (n,m) <- [(head (words w), words w !! 1)]]

parseWords :: [String] -> Int -> [String]
parseWords xs y = take y xs

takeLast4 :: String -> String
takeLast4 s = drop (length s - min 4 (length s)) s

takeFirst5 :: String -> String
takeFirst5 = take 5

checkPath :: [Char] -> [Char] -> Bool
checkPath a b = all (`elem` takeFirst5 b) (takeLast4 a)


createGraph :: [String] -> Graph
createGraph xs =
        let graphList = mapMaybe (\x ->
                        let neighbors = [y |  y <- xs, y /= x, checkPath x y ]
                        in if null neighbors
                            then Nothing
                            else Just (x, neighbors)
                        ) xs
        in Map.fromList graphList


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

-- >>>for_ results $ \x -> putStrLn (if x < 0 then "Impossible" else show x)

-- 
-- 
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






