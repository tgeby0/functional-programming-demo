sumPowers :: Int -> [Int] -> Int
sumPowers _ [] = 0
sumPowers power (x : xs) = (x ^ power) + sumPowers power xs

sumPowers2 = sumPowers 2
sumPowers3 = sumPowers 3

sum1 = sumPowers2 [1, 2, 3, 4] -- 30
sum2 = sumPowers3 [1, 2, 3, 4] -- 100

main = do
    print sum1
    print sum2