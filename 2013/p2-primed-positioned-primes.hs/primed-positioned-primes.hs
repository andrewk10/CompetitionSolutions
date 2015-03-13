main = do (a : b : n : []) <- fmap (map read . words) getLine :: IO [Int]
          putList $ superPrimes a b n

-- putList ns : print the list of integers
putList :: [Int] -> IO ()
putList ns = case ns of []      -> putStrLn ""
                        [n]     -> putStrLn $ show n
                        (n:ns') -> do putStr $ show n
                                      putChar ' '
                                      putList ns'

-- primes : the ascending list of prime numbers
primes :: [ Int ]
primes = 2 : filter isPrime [3, 5 ..]

-- isPrime n : is integer 'n' prime?
isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = all (\p -> n `mod` p /= 0) $ takeWhile (\p -> p ^ 2 <= n) primes

-- superPrimes a b n : the super prime list of order 'n', using the primes
--                     between 'a' and 'b' inclusive as base case
superPrimes :: Int -> Int -> Int -> [Int]
superPrimes a b 0 = takeWhile (<= b) $ dropWhile (< a) primes
superPrimes a b n = [ p | (i, p) <- zip [1..] (superPrimes a b (n - 1))
                        , isPrime i ]
