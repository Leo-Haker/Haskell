import Text.Read (readMaybe)
import Data.Maybe
import Control.Concurrent.STM (check)


main :: IO ()
main = do
    input <- getContents
    let ls = lines input                 -- dela upp input i rader
        numbers = parseNumbers (head ls) -- första raden → tal
        restLines = tail ls
        words = parseWords restLines (head numbers)
        paths = parsePaths restLines (head numbers)
        graph = createGraph words paths
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
 

