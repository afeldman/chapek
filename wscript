#! /usr/bin/env python3
# encoding: utf-8
# Anton Feldmann, 2023

import os

top = '.'
out = 'build'

def options(opt):
        pass

def configure(conf):
	try:
		conf.find_program('ktrans', var='KTRANS')
	except conf.errors.ConfigurationError:
		conf.fatal('could not find ktrans')

def build(bld):
	bld(rule='${KTRANS} ${SRC} ${TGT}', source='src/capek.kl', target='capek.pc')

def deploy(bld):
	os.system('ftp -s:deploy.ftp localhost')
