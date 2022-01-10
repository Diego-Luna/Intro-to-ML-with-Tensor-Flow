# 🧪 Quiz: Bayes Rule

Suppose you have a bag with three standard 6-sided dice with face values [1,2,3,4,5,6] and two non-standard 6-sided dice with face values [2,3,3,4,4,5]. Someone draws a die from the bag, rolls it, and announces it was a 3. What is the probability that the die that was rolled was a standard die?

Input your answer as a fraction or as a decimal with at least three digits of precision.

## 💻 Process

1. `P (A | B) = P (A ^ B) / P (B). Also P (B | A) = P (B ^ A) / P (A).`

2. Try to draw a graphy like

```
Standard says p = 3/5 ---- number 3 p = 1/6
                                      ---- Non-number 3 p = 5/6
Non-standard says p = 2/5 ---- number 3 p = 2/6
                                               ----- Non-number 3 p = 4/6
```

3. Now you got P (standard dice), P (non-standard dice), P ('3' | standard dice), P ('3' | non-standard dice), use the naive bayes formula:

```
3/5 \* 1/6 = 3/30

2/5 \* 2/6 = 4/30

3/30 + 4/30 = 7/30

(3/5 \* 1/6)/(7/30) = ( 3/30)/(7/30)

3/30 \* 30/7 =3/7
```

Result: `3/7`
