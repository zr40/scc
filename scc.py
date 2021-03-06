#!/usr/bin/python

import os
import sys

import json

from optparse import OptionParser, OptionGroup

from compiler import SCCompiler, CompilerError

def main():
	usage = 'usage: %prog [options]'
	description = 'Compiles main.sc and its dependencies to assembly.'
	epilog = 'Report bugs and feature requests to zr40.nl@gmail.com'
	version = '%prog 0.3 dev'
	parser = OptionParser(usage=usage, description=description, epilog=epilog, version=version)
	parser.add_option('-m', metavar='PATH', action='append', dest='moduleSearchPath', help='look for referenced modules in PATH', default=[])
	parser.add_option('--no-opt', action='store_false', dest='optimize', help='do not perform optimizations', default=True)
	parser.add_option('-v', action='store_true', dest='verboseinfo', help='show verbose information', default=False)
	parser.add_option('-p', action='store_true', dest='verboseprogress', help='show verbose progress', default=False)

	group = OptionGroup(parser, 'Debugging options')
	group.add_option('--debug-compiler', action='store_true', dest='debugCompiler', help='show a stack trace for compile errors', default=False)
	group.add_option('--debug-parser', action='store_true', dest='debugParser', help='write yacc debug output to parser.out', default=False)
	group.add_option('--debug-codegen', action='store_true', dest='debugCodeGenerator', help='keep syntax comments in output when optimizing', default=False)
	group.add_option('--debug-optimizer', action='store_true', dest='debugOptimizer', help='allow optimizer to show diagnostic messages', default=False)

	parser.add_option_group(group)

	options, args = parser.parse_args()

	if args:
		parser.error("no such option: %s" % args[0])

	if not os.path.exists('main.sc'):
		parser.error("'main.sc' does not exist")

	def compile():
		return SCCompiler().compile(options)

	if options.debugCompiler:
		asm, debugData = compile()
	else:
		try:
			asm, debugData = compile()
		except CompilerError as e:
			print e
			sys.exit(1)

	with open('output.asm', 'w') as outputfile:
		outputfile.write(asm)

	with open('output.scdebug', 'w') as outputfile:
		outputfile.write(debugData)

if __name__ == '__main__':
	main()
