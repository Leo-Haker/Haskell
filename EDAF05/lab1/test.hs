import Data.List (all)

fun :: Num a => a -> a -> a
fun x y = x + y


--checkWordLength :: [Char] -> Bool
--checkWordLength word = if length word == 5 then checkPath word else False

takeLast4 :: String -> String
takeLast4 s = drop (length s - min 4 (length s)) s

takeFirst5 :: String -> String
takeFirst5 s = take 5 s

checkPath :: [Char] -> [Char] -> Bool
checkPath a b = all (`elem` first5B) last4A
    where 
        last4A = takeLast4 a
        first5B = takeFirst5 b

--all :: (a -> Bool) -> [a] -> Bool Tar en predikatfunktion 
-- och en lista, och returnerar True om predikatet är sant för alla element i listan, annars False.
-- elem :: Eq a => a -> [a] -> Bool Tar ett element och en lista, och returnerar True om elementet finns i listan, annars False.
-- Eq är en typklass i Haskell som definierar en ekvivalensrelation mellan värden av en viss typ. Det innebär att typer som är instanser av Eq kan jämföras för likhet med hjälp av operatorn (==) och (/=).

--selectedChars :: String
--selectedChars = [ String !! i | i <- [1,2,3,4] ]