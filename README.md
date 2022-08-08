# Galois Field

## modular polynomals
```
         111
	 1011
	 10011
	 100101
	 1000011
	 10001001
	 100011101
	 1000010001
	 10000001001
```

## package testing

```
from GaloisField import gf

#construction of Galois Field GF(2³)
m = 3
GF
>>> GF(2³)
```

### polynomial representation

```
GF.modPol_pr()
>>> α³ + α¹ + α⁰
```
### vector representation

```
GF.modPol_vr()
>>> 1011
```

### alpha elements
```
alphas = GF.getElements()
alphas
>>> [001, 010, 100, 011, 110, 111, 101]
```

### vector representation
```
alphas[1]
>>> 010
```

### polynomial representation
```
alphas[1].getAlpha()
>>> α¹
```

## operations

### 1. addition
```
alphas[0] + alphas[1]
>>> 011
```

### 2. multiplication
```
alphas[1] * alphas[2]
>>> 011
```

### 3. inverse
```
- alphas[1]
>>> 101
```

### 4. division
```
alphas[5] / alphas[2]
>>> 011
```

### 5. exponent
```
alphas[2] ** 3
>>> 101
```
