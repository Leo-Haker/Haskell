import Text.Read (readMaybe)
import qualified Data.Set as Set
import Data.Sequence (Seq, (|>), (<|))
import qualified Data.Sequence as Seq
import qualified Data.Map as Map
import Data.Maybe
import Control.Concurrent.STM (check)
import qualified Data.Binary.Builder as Seq


main :: IO ()
main = do
    input <- getContents
    let ls = lines input                 -- dela upp input i rader
        numbers = parseNumbers (head ls) -- första raden → tal
        restLines = tail ls
        words = parseWords restLines (head numbers)
        paths = parsePaths restLines (head numbers)
        graph = createGraph2 words

        --  
    print numbers
    print words
    print paths

-- Konverterar en sträng med mellanslag till [Int], ignorerar icke-tal
parseNumbers :: String -> [Int]
parseNumbers s = [n | w <- words s, Just n <- [readMaybe w :: Maybe Int]]

parsePaths :: [String] -> Int -> [(String, String)]
parsePaths xs y = 
    let brute = drop y xs
    in  [(n,m) | w <- brute, (n,m) <- [(head(words w), words w !! 1)]]

parseWords :: [String] -> Int -> [String]
parseWords xs y = take y xs

createGraph :: [String] -> [(String, String)] -> [(String, [String])]
createGraph xs ys = 
        mapMaybe (\x -> 
                        let forward = [snd y | y <- ys, fst y == x, uncurry checkPath y]
                            backward = [fst y | y <- ys, snd y == x, uncurry checkPath y]
                            neighbors = forward ++ backward
                        in if null neighbors
                            then Nothing 
                            else Just(x, neighbors)
                        )xs

takeLast4 :: String -> String
takeLast4 s = drop (length s - min 4 (length s)) s

takeFirst5 :: String -> String
takeFirst5 = take 5

checkPath :: [Char] -> [Char] -> Bool
checkPath a b = all (`elem` takeFirst5 b) (takeLast4 a)


{- TODO: Implementera BFS för att hitta kortaste vägen mellan start och mål i grafen. 
         Använd en kö (queue) för att hålla reda på vilka noder som ska besökas härnäst, och en mängd (set) för att hålla reda på vilka noder som redan har besökts. 
         När du når målet, returnera längden på den kortaste vägen.
   
   Funktionell while loop i Haskell 
   loop state =
    if done
        then state
        else
            let state' = update state
            in loop state' 

    foldl f startvärde lista
    f = funktion som uppdaterar ett värde
    startvärde = initialt state
    lista = elementen du går igenom

    foldl (+) 0 [1,2,3,4] == ((((0 `f` 1) `f` 2) `f` 3) `f` 4)

    Mål:
    foldl processNeighbor state neighbors

-}

--TEST
type Visited = Set.Set String
type Queue = Seq.Seq String
type Path = [String]
type State = (Visited, Queue, Path)
type Graph = Map.Map String [String]

getPathLength :: State -> Int
getPathLength (_, _, path) = length path

--FUNKAR
-- >>> createGraph2 ["abcde", "bcdef", "cdefg", "defgh", "efghi"]
-- fromList [("abcde",["bcdef"]),("bcdef",["cdefg"]),("cdefg",["defgh"]),("defgh",["efghi"])]
createGraph2 :: [String] -> Graph
createGraph2 xs = 
        let graphList = mapMaybe (\x -> 
                        let neighbors = [y |  y <- xs, y /= x, checkPath x y ]
                        in if null neighbors
                            then Nothing 
                            else Just(x, neighbors)
                        )xs
        in Map.fromList graphList


popSeq :: Seq a -> Maybe (a, Seq a)
popSeq q =
    case Seq.viewl q of
        Seq.EmptyL   -> Nothing
        x Seq.:< q'  -> Just (x, q')

neighbors :: Graph -> String -> [String]
neighbors graph node = Map.findWithDefault [] node graph

addToQueue :: (Queue, Visited) -> [String] -> (Queue, Visited)
addToQueue (queue, visited) neighbors = foldl (\(q, v) n -> if Set.member n visited then (q, v) else (q Seq.|> n, Set.insert n v)) (queue, visited) neighbors

bfs :: State -> Graph -> (String, String) -> State
bfs (visited, queue, path) graph (start, goal) =
    if start == goal
        then (visited, queue, path)
    else 
        if Set.member start visited
            then
                let
                    Just(st, q) = popSeq queue
                in
                    bfs (visited, q, path) graph (st, goal)
        else
            let 
                v = Set.insert start visited
                p = path : start
            in
                let neighbors = neighbors graph start 
                    (q, v) = foldl addToQueue (queue, visited) neighbors
                    Just(st'', q'') =  popSeq q
                   
                in 
                    
                    
                    
                    

                
                    





