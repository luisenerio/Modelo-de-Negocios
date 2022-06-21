



#Lectura de Datos

library(tidyverse)
datos1 <- read_csv("AumentadaPFLD.csv")
datos_m <- as.matrix(datos1)

escalar <- function(vector){
  resultado <- (vector-mean(vector))/sd(vector)
  return(resultado)
}


datos1_center <- datos1 %>% mutate_all(~escalar(.))


m_cov <- cov(datos1_center)#matriz de correlaciones

eigen <- eigen(m_cov)
eigenvalores <- eigen$values
eigenvectores <- eigen$vectors


acp_cov <- prcomp(datos1,center = T,scale. = F)
summary(acp_cov)

desviaciones <- as.matrix(acp_cov$sdev)[1:2,]
varianza <- desviaciones*desviaciones
Componenetes <- acp_cov$rotation[,1:2]
Componenetes_cuadrado <- Componenetes*Componenetes

Riesgos <- ((datos_m %*% Componenetes_cuadrado[,1])*varianza[1]+(datos_m %*% Componenetes_cuadrado[,2])*varianza[2])/sum(varianza)

plot(Riesgos)

plot(acp_cov$x[,1],acp_cov$x[,2])

plot(acp_cov$x[,1],acp_cov$x[,30])




datos <- data.frame(Riesgos,acp_cov$x[,1],acp_cov$x[,2],acp_cov$x[,3], acp_cov$x[,29],acp_cov$x[,30])
write_csv(datos,"C:\\Users\\User\\Desktop\\Modelo-de-Negocios\\ACP\\datos.csv")







