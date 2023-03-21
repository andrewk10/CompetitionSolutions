import Control.Applicative ( (<$>) )
import Control.Monad       ( replicateM_ )

main :: IO ()
main = do n <- read <$> getLine :: IO Int
          replicateM_ n calcOne

-- calcOne : process one line of input
calcOne :: IO ()
calcOne =
    words <$> getLine >>= \(_ : ts) ->
    if eval ts []
    then print 1
    else print 0

-- Op : a Boolean operator
data Op = And | Or | Xor | Not

-- eval ts bs : the result of evaluating the list of tokens 'ts'
--              using Boolean stack 'bs'
eval :: [String] -> [Bool] -> Bool
eval []       [b] = b
eval (t : ts) bs
    | t == "0"    = eval ts $ False : bs
    | t == "1"    = eval ts $ True  : bs
    | t == "A"    = eval ts $ apply And bs
    | t == "R"    = eval ts $ apply Or  bs
    | t == "X"    = eval ts $ apply Xor bs
    | t == "N"    = eval ts $ apply Not bs
    | otherwise   = error "eval : invalid token"
eval _        _   = error "eval : incompatible arguments"

-- apply op bs : the Boolean stack obtained by applying Boolean operator 'op'
--               on the Boolean stack 'bs'
apply :: Op -> [Bool] -> [Bool]
apply And (b1 : b2 : bs) = let b = b1 && b2 in b `seq` b : bs
apply Or  (b1 : b2 : bs) = let b = b1 || b2 in b `seq` b : bs
apply Xor (b1 : b2 : bs) = let b = b1 /= b2 in b `seq` b : bs
apply Not (b : bs)       = let b' = not b in b' `seq` b' : bs
apply _   _              = error "apply : invalid argument(s)"
