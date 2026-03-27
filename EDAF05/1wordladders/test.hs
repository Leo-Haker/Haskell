-- LÄS! checka funktionerna "takeWhile" och "dropWhile" i Prelude, och fundera på hur de kan användas i det här sammanhanget.

import Data.List (all)
import Data.Maybe

---------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
printHello :: IO()
printHello = print "Hello"

-- putStrLn :: String -> IO() 
-- getLine IO String (slutar efter ny rad)
-- För att läsa in flera rader se följande
main :: IO()
main = do
    input <- getContents
    print (input)

createGraph'' :: [String] -> [(String, String)] -> [(String, [String])]
createGraph'' xs ys = 
        mapMaybe (\a -> 
                        let matches = [snd b | b <- ys, fst b == a, checkPath (fst b) (snd b) == True]
                        in if null matches 
                            then Nothing
                            
                            else 
                                let reverseMatches = [fst b | b <- ys, snd b == a, checkPath (snd b) (fst b) == True]
                                in if null reverseMatches
                                then Just (a, matches)
                                else Just (a, matches ++ reverseMatches)
                        )xs

        
createGraph :: [String] -> [(String, String)] -> [(String, [String])]
createGraph xs ys = 
        mapMaybe (\x -> 
                        let forward = [snd y | y <- ys, fst y == x, checkPath (fst y) (snd y) == True]
                            backward = [fst y | y <- ys, snd y == x, checkPath (snd y) (fst y) == True]
                            neighbors = forward ++ backward
                        in if null neighbors
                            then Nothing 
                            else Just(x, neighbors)
                        )xs



takeLast4 :: String -> String
takeLast4 s = drop (length s - min 4 (length s)) s

takeFirst5 :: String -> String
takeFirst5 s = take 5 s

checkPath :: [Char] -> [Char] -> Bool
checkPath a b = all (`elem` first5B) last4A
    where 
        last4A = takeLast4 a
        first5B = takeFirst5 b


-- Stack
data Stack a = Stack [a] deriving Show

empty :: Stack a
empty = Stack []

push :: a -> Stack a -> Stack a
push x (Stack xs) = Stack (x:xs)

pop :: Stack a -> (Maybe a, Stack a)
pop (Stack []) = (Nothing, Stack[])
pop (Stack(x:xs)) = (Just x, Stack(xs))