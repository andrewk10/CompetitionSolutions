-- Note: Generated by ChatGPT, I don't know Haskell :)

import System.IO
import Data.List

-- ------------------------------------------
-- 1. FUNCTION parse_in
-- ------------------------------------------
parseIn :: Handle -> IO [Int]
parseIn myInputStream = do
  -- 1. We create the output variable
  let res = []

  -- 2. We get the number of test cases
  numTestCasesStr <- hGetLine myInputStream
  let numTestCases = read numTestCasesStr :: Int

  -- 3. We get the list of test cases
  replicateM numTestCases $ do
    -- 3.1. We get the line
    line <- hGetLine myInputStream

    -- 3.2. We append it to res
    return $ read line

-- ------------------------------------------
-- 2. FUNCTION parse_out
-- ------------------------------------------
parseOut :: Handle -> [(Int, Int)] -> IO ()
parseOut myOutputStream outputInfo = do
  -- 1. We traverse outputInfo so as to print it
  let indexedOutputInfo = zip outputInfo [1..]
  forM_ indexedOutputInfo $ \((item1, item2), index) -> do
    -- 2.1. We create the line to write
    let myStr = "Case #" ++ show index ++ ": " ++ show item1 ++ " " ++ show item2 ++ "\n"

    -- 2.2. We print the line
    hPutStr myOutputStream myStr

-- ------------------------------------------
-- 3. FUNCTION strategy
-- ------------------------------------------
strategy :: [Int] -> [(Int, Int)]
strategy inputInfo = do
  -- 1. We create the output variable
  let res = []

  -- 2. We solve the different test cases
  for n <- inputInfo do
    -- 2.1. We set up a and b
    let found = False
    let a = 1
    let b = n-1

    -- 2.2. We traverse the posibilities until we find a valid one
    let results = take 1 [(a', b') | a' <- [a..b], b' <- [a..b], "4" `notElem` show a' && "4" `notElem` show b']

    -- 2.3. We append the solution to the list
    let (a'', b'') = if null results then (0, 0) else head results
    res ++ [(a'', b'')]

  -- 3. We return res
  return res
