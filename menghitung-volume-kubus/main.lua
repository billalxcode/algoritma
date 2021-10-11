-- 2021-10-11
-- pandas id


print("Panjang kubus: ")
local panjang = io.read("*n")

if type(panjang) == 'number' then
  local volume = panjang*panjang*panjang
  print("volume kubus: "..volume)
end
