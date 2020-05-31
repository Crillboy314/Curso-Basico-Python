### Distribuciones de probabilidad

## Distribucion de Bernoulli

from scipy import stats

p = 0.5
bernoulliDist = stats.bernoulli(p)

p_tails = bernoulliDist.pmf(0) 
p_heads = bernoulliDist.pmf(1)

print(p_tails, p_heads)

#Generacion de Aleatorios

trials = bernoulliDist.rvs(10)
print(trials)

## Distribucion Binomial

(p, num) = (0.5, 4)
binomDist = stats.binom(num, p)

print(binomDist.pmf(np.arange(5)))

## Distribucion Normal

from scipy.stats import norm

# Generacion de distribucion 

mu=-2
sigma = 0.7
myDistribution = stats.norm(mu, sigma) 
significanceLevel = 0.05
print(myDistribution.ppf([significanceLevel/2, 1-significanceLevel/2] ))
print(myDistribution.interval(0.95))


# Generacion de aleatorios

r = norm.rvs(size=100)
print(r)

#### Problema con prueba de hipotesis

## De entre todos los ninios nacidos vivos en los Estados Unidos, se 
## recolecta la siguiente informacion:
## Media de 3.5 y 0.76 como desviacion estandar
## Se puede decir que un ninio que nacio con un peso de 2.6 kg
## Pertenece al grupo de los ninios sanos ?


nd = stats.norm(3.5, 0.76)
print(nd.cdf(2.6))

# Se puede utilizar directamente la funcion de distribucion acumulada.
# En este caso, para el valor de 2.6 obtenemos como respuesta cerca
# del 11 por ciento de los datos acumulados hasta ese punto, lo que en
# dependencia de la significancia que se escoja me conduce a la 
# conclusion de si pertenece o no al grupo de los sanos.