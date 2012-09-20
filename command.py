#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2012 liy <liy@liy-desktop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import expect

class CommandBase:
	def preexec(self):
		pass
	
	def exec(self, out, **args):
		pass
	
	def postexec(self):
		pass
	
	def stop(self):


class SimpleCommand(CommandBase):
	cmds=""
	child=None
	def __init__(self, cmds):
		self.cmds = cmds
	
	def exec(self, out, **args):
		child = pexpect.spawn ('/bin/bash', ['-c', self.cmds], timeout=600)
		self.child = child
		while True:
			try:
				i = child.readline()
				if i:
					out.write(i.rstrip())
				elif child.eof():
					out.write("eof")
					break
				else:
					break
			except pexpect.EOF:
				out.write("eof")
				break
			except pexpect.TIMEOUT as e:
				out.write("exception timeout, checkout backgroud progress")
				break
		child.close(force=True)
	
	def stop(self):
		if self.child.

def main():
	
	return 0

if __name__ == '__main__':
	main()

