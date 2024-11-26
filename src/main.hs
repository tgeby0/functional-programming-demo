-- Write printAMessage here
printAMessage :: Show a => a -> IO ()
printAMessage a = print a
-- Write division here
division :: Double -> Double -> Maybe Double
division _ 0 = Nothing
division x y = Just (x/y)
-- Write factorial here
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)
-- Write factList here
factList :: Int -> [Int]
factList n = map factorial [1..n]
-- Write merge here
merge :: [Int] -> [Int] -> [Int]
merge [] [] = []
merge (a:as) [] = a : merge as []
merge [] (a:as) = a : merge [] as
merge (a:as) (b:bs) 
    | a < b = a : merge as (b:bs)
    | otherwise = b : merge (a:as) bs

main = do
    printAMessage "b" -- Replace this with your testing code
    print (division 3 0)
    print (factorial 5)
    print (factList 5)
    print (merge [1,2,3,7] [2,4,8])
    print (merge [8,456,4567] [1,2,3])
    print (merge [1,2,3,4] [1,2,3,4])
    print (merge [0,1,6] [4,5,6,7])