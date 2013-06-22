#!#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system import messages

# Esto solo se ejecuta cuando es llamado como programa principal
if __name__ == '__main__':
	mostrar = messages.error(None, messages.FOLDER_NOK)
	print mostrar
	
	mostrar = messages.aviso(None, mensajes.OPER_OK)
	print mostrar

	mostrar = messages.pregunta(None, '¿Desea continuar?')
	print mostrar

	mostrar = messages.advert(None, 'Cuidado!!' + '\n' + '¿Desea continuar?')
	print mostrar
