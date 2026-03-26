-- LÄS! checka funktionerna "takeWhile" och "dropWhile" i Prelude, och fundera på hur de kan användas i det här sammanhanget.

import Data.List (all)
import Data.Maybe

fun :: Num a => a -> a -> a
fun x y = x + y


--checkWordLength :: [Char] -> Bool
--checkWordLength word = if length word == 5 then checkPath word else False



--all :: (a -> Bool) -> [a] -> Bool Tar en predikatfunktion 
-- och en lista, och returnerar True om predikatet är sant för alla element i listan, annars False.
-- elem :: Eq a => a -> [a] -> Bool Tar ett element och en lista, och returnerar True om elementet finns i listan, annars False.
-- Eq är en typklass i Haskell som definierar en ekvivalensrelation mellan värden av en viss typ. Det innebär att typer som är instanser av Eq kan jämföras för likhet med hjälp av operatorn (==) och (/=).

--selectedChars :: String
--selectedChars = [ String !! i | i <- [1,2,3,4] ]

a = [x*y | x <- [1,2,3], y <- [4,5,6]]
xxs = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]] 
b :: [[Integer]] -> [[Integer]]
b' :: [[Integer]] -> [[Integer]]
b xxs = [ [ x | x <- xs, even x ] | xs <- xxs]
b' xxs = map (filter even) xxs

word = ["jagar", "hejar", "kulig", "ahaaa"]
path = [("jagar", "gajar"), ("jagar", "kulig"), ("kulig", "gulli"), ("jagar", "hagar"), ("jagar","ragga")]

test :: [String] -> [(String, String)] -> ([String], [(String, String)])
test a b = (a,b)


test' :: [String] -> [(String, String)] -> [(String, [(String, String)])]
test' xs ys = 
        mapMaybe (\a -> 
                        let matches = [b | b <- ys, fst b == a]
                        in if null matches 
                            then Nothing
                            else Just (a, matches)
                        )xs

-- målet är en lista av tuples. Maybe [(String, [(String, String)])]




-- SE NEDAN!
test'' :: [String] -> [(String, String)] -> [(String, [(String, String)])]
test'' xs ys = 
        mapMaybe (\a -> 
                        let matches = [b | b <- ys, fst b == a, checkPath (fst b) (snd b) == True]
                        in if null matches 
                            then Nothing
                            else Just (a, matches)
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