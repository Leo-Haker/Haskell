import Data.Word (Word32)
import Data.List (foldl')
import Text.XHtml.Transitional (table)

-- Daniel J. Bernstein hash
-- hanterar overflow (wraps around), undviker minnesproblem edm foldl' 
djb2 :: String -> Word32
djb2 = foldl' step 5381
  where
    step :: Word32 -> Char -> Word32
    step hash char = (hash * 33) + fromIntegral (fromEnum char)

hashIndexDjb :: String -> Int -> Int
hashIndexDjb string tableSize = flip mod tableSize $ fromIntegral $ djb2 string

-- egen version av djb
hashString :: String -> Int
hashString = foldl'(\acc c -> acc * 33 + fromEnum c) 5381 

hashIndex :: String -> Int -> Int 
hashIndex string tableSize = hashString string `mod` tableSize
