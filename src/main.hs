

-- Calls a function on a Maybe value if it exists, returning the result, or returns a default value otherwise
callOrDefault :: (a -> b) -> b -> Maybe a -> b
callOrDefault fn _ (Just x) = fn x
callOrDefault _ defaultValue Nothing = defaultValue

main = print (callOrDefault (*2) 5 (Nothing))