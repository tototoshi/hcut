#!/usr/bin/env python
# -*- coding: utf-8 -*-
import errno
import sys
import fileinput
import argparse

__author__  = "Toshiyuki Takahashi"
__version__ = "0.1.2"
__license__ = "BSD License"

DEFAULT_SEPARATOR = "\t"

class FieldNotFoundError(Exception):
    pass

def _get_field_index(field, header_fields):
    i = 0
    for hf in header_fields:
        if field == hf:
            return i
        i += 1
    raise FieldNotFoundError("%s not found" % (field,))

def _get_all_fields_indices(fields, header_fields):
    res = []
    for field in fields:
        res.append(_get_field_index(field, header_fields))
    return res

def _extract_fields_from_line(field_indices, line, separator):
    line = line.rstrip()
    fields = line.split(separator)

    cutted = []
    for index in field_indices:
        if len(fields) > index:
            cutted.append(fields[index])
        else:
            cutted.append("")

    return cutted

def cut_stdin(target_fields, print_header=False, separator=DEFAULT_SEPARATOR, encoding="utf-8"):
    for line in reader(target_fields, sys.stdin, print_header, separator, encoding):
        print separator.join(line)

def cut_files(target_fields, input_files, print_header=False, separator=DEFAULT_SEPARATOR, encoding="utf-8"):
    for input_file in input_files:
        f = open(input_file)
        try:
            for line in reader(target_fields, f, print_header, separator, encoding):
                print separator.join(line)
                # print header only once
                print_header = False
        finally:
            f.close()


class reader(object):

    def __init__(self, target_fields, file_obj, print_header, separator, encoding):
        header = file_obj.next()
        header_fields = header.rstrip().split(separator)
        header_fields = [unicode(h, encoding) for h in header_fields]
        self._pos = 0
        self._separator = separator
        self._print_header = print_header
        self._field_indices = _get_all_fields_indices(target_fields, header_fields)
        self._cutted_header = _extract_fields_from_line(self._field_indices, header, separator=self._separator)
        self._file_obj = file_obj

    def __iter__(self):
        return self

    def next(self):
        if self._pos == 0 and self._print_header:
            self.print_header = False
            self._pos += 1
            return self._cutted_header
        else:
            self._pos += 1
            return _extract_fields_from_line(self._field_indices,
                                             self._file_obj.next(),
                                             separator=self._separator)
