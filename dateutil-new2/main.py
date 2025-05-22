 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import dateutil.easter

import itertools

import dateutil.rrule

import pytest

import dateutil

import datetime

import dateutil.parser

import dateutil.utils

import sys

import dateutil.tzwin

import dateutil.relativedelta

import dateutil.zoneinfo

import time

import dateutil.tz

import six

import gc


app = Flask(__name__)

# Function Definitions

def main(metadata_file):
    """Auto-generated function: main"""
    try:
        response = dateutil.updatezinfo.main(metadata_file)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run():
    """Auto-generated function: run"""
    try:
        response = dateutil.setup.Unsupported.run()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def README():
    """Auto-generated function: README"""
    try:
        response = dateutil.setup.README()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def easter(year, method):
    """Auto-generated function: easter"""
    try:
        response = dateutil.easter.easter(year, method)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def today(tzinfo):
    """Auto-generated function: today"""
    try:
        response = dateutil.utils.today(tzinfo)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def default_tzinfo(dt, tzinfo):
    """Auto-generated function: default_tzinfo"""
    try:
        response = dateutil.utils.default_tzinfo(dt, tzinfo)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def within_delta(dt1, dt2, delta):
    """Auto-generated function: within_delta"""
    try:
        response = dateutil.utils.within_delta(dt1, dt2, delta)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def weeks(value):
    """Auto-generated function: weeks"""
    try:
        response = dateutil.relativedelta.relativedelta.weeks(value)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def normalized():
    """Auto-generated function: normalized"""
    try:
        response = dateutil.relativedelta.relativedelta.normalized()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def count():
    """Auto-generated function: count"""
    try:
        response = dateutil.rrule.rrulebase.count()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def before(dt, inc):
    """Auto-generated function: before"""
    try:
        response = dateutil.rrule.rrulebase.before(dt, inc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def after(dt, inc):
    """Auto-generated function: after"""
    try:
        response = dateutil.rrule.rrulebase.after(dt, inc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def xafter(dt, count, inc):
    """Auto-generated function: xafter"""
    try:
        response = dateutil.rrule.rrulebase.xafter(dt, count, inc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def between(after, before, inc, count):
    """Auto-generated function: between"""
    try:
        response = dateutil.rrule.rrulebase.between(after, before, inc, count)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def replace():
    """Auto-generated function: replace"""
    try:
        response = dateutil.rrule.rrule.replace()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def rebuild(year, month):
    """Auto-generated function: rebuild"""
    try:
        response = dateutil.rrule._iterinfo.rebuild(year, month)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def ydayset(year, month, day):
    """Auto-generated function: ydayset"""
    try:
        response = dateutil.rrule._iterinfo.ydayset(year, month, day)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mdayset(year, month, day):
    """Auto-generated function: mdayset"""
    try:
        response = dateutil.rrule._iterinfo.mdayset(year, month, day)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def wdayset(year, month, day):
    """Auto-generated function: wdayset"""
    try:
        response = dateutil.rrule._iterinfo.wdayset(year, month, day)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def ddayset(year, month, day):
    """Auto-generated function: ddayset"""
    try:
        response = dateutil.rrule._iterinfo.ddayset(year, month, day)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def htimeset(hour, minute, second):
    """Auto-generated function: htimeset"""
    try:
        response = dateutil.rrule._iterinfo.htimeset(hour, minute, second)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mtimeset(hour, minute, second):
    """Auto-generated function: mtimeset"""
    try:
        response = dateutil.rrule._iterinfo.mtimeset(hour, minute, second)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def stimeset(hour, minute, second):
    """Auto-generated function: stimeset"""
    try:
        response = dateutil.rrule._iterinfo.stimeset(hour, minute, second)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def rrule(rrule):
    """Auto-generated function: rrule"""
    try:
        response = dateutil.rrule.rruleset.rrule(rrule)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def rdate(rdate):
    """Auto-generated function: rdate"""
    try:
        response = dateutil.rrule.rruleset.rdate(rdate)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def exrule(exrule):
    """Auto-generated function: exrule"""
    try:
        response = dateutil.rrule.rruleset.exrule(exrule)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def exdate(exdate):
    """Auto-generated function: exdate"""
    try:
        response = dateutil.rrule.rruleset.exdate(exdate)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def instance(cls):
    """Auto-generated function: instance"""
    try:
        response = dateutil.tz._factories._TzFactory.instance(cls)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tzname_in_python2(namefunc):
    """Auto-generated function: tzname_in_python2"""
    try:
        response = dateutil.tz._common.tzname_in_python2(namefunc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def is_ambiguous(dt):
    """Auto-generated function: is_ambiguous"""
    try:
        response = dateutil.tz._common.tzrangebase.is_ambiguous(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def fromutc(dt):
    """Auto-generated function: fromutc"""
    try:
        response = dateutil.tz._common.tzrangebase.fromutc(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def utcoffset(dt):
    """Auto-generated function: utcoffset"""
    try:
        response = dateutil.tz._common.tzrangebase.utcoffset(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def dst(dt):
    """Auto-generated function: dst"""
    try:
        response = dateutil.tz._common.tzrangebase.dst(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tzname(dt):
    """Auto-generated function: tzname"""
    try:
        response = dateutil.tz._common.tzrangebase.tzname(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def utcoffset(dt):
    """Auto-generated function: utcoffset"""
    try:
        response = dateutil.tz.tz._tzicalvtz.utcoffset(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def dst(dt):
    """Auto-generated function: dst"""
    try:
        response = dateutil.tz.tz._tzicalvtz.dst(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tzname(dt):
    """Auto-generated function: tzname"""
    try:
        response = dateutil.tz.tz._tzicalvtz.tzname(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def is_ambiguous(dt, idx):
    """Auto-generated function: is_ambiguous"""
    try:
        response = dateutil.tz.tz.tzfile.is_ambiguous(dt, idx)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def fromutc(dt):
    """Auto-generated function: fromutc"""
    try:
        response = dateutil.tz.tz.tzfile.fromutc(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def transitions(year):
    """Auto-generated function: transitions"""
    try:
        response = dateutil.tz.tz.tzrange.transitions(year)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def keys():
    """Auto-generated function: keys"""
    try:
        response = dateutil.tz.tz.tzical.keys()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get(tzid):
    """Auto-generated function: get"""
    try:
        response = dateutil.tz.tz.tzical.get(tzid)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def datetime_exists(dt, tz):
    """Auto-generated function: datetime_exists"""
    try:
        response = dateutil.tz.tz.datetime_exists(dt, tz)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def datetime_ambiguous(dt, tz):
    """Auto-generated function: datetime_ambiguous"""
    try:
        response = dateutil.tz.tz.datetime_ambiguous(dt, tz)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def resolve_imaginary(dt):
    """Auto-generated function: resolve_imaginary"""
    try:
        response = dateutil.tz.tz.resolve_imaginary(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def load_name(offset):
    """Auto-generated function: load_name"""
    try:
        response = dateutil.tz.win.tzres.load_name(offset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def name_from_string(tzname_str):
    """Auto-generated function: name_from_string"""
    try:
        response = dateutil.tz.win.tzres.name_from_string(tzname_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def list():
    """Auto-generated function: list"""
    try:
        response = dateutil.tz.win.tzwinbase.list()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def display():
    """Auto-generated function: display"""
    try:
        response = dateutil.tz.win.tzwinbase.display()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def transitions(year):
    """Auto-generated function: transitions"""
    try:
        response = dateutil.tz.win.tzwinbase.transitions(year)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def picknthweekday(year, month, dayofweek, hour, minute, whichweek):
    """Auto-generated function: picknthweekday"""
    try:
        response = dateutil.tz.win.picknthweekday(year, month, dayofweek, hour, minute, whichweek)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def valuestodict(key):
    """Auto-generated function: valuestodict"""
    try:
        response = dateutil.tz.win.valuestodict(key)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def isoparse(dt_str):
    """Auto-generated function: isoparse"""
    try:
        response = dateutil.parser.isoparser.isoparser.isoparse(dt_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def parse_isodate(datestr):
    """Auto-generated function: parse_isodate"""
    try:
        response = dateutil.parser.isoparser.isoparser.parse_isodate(datestr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def parse_isotime(timestr):
    """Auto-generated function: parse_isotime"""
    try:
        response = dateutil.parser.isoparser.isoparser.parse_isotime(timestr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def parse_tzstr(tzstr, zero_as_utc):
    """Auto-generated function: parse_tzstr"""
    try:
        response = dateutil.parser.isoparser.isoparser.parse_tzstr(tzstr, zero_as_utc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_token():
    """Auto-generated function: get_token"""
    try:
        response = dateutil.parser._parser._timelex.get_token()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def next():
    """Auto-generated function: next"""
    try:
        response = dateutil.parser._parser._timelex.next()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def split(cls, s):
    """Auto-generated function: split"""
    try:
        response = dateutil.parser._parser._timelex.split(cls, s)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def isword(cls, nextchar):
    """Auto-generated function: isword"""
    try:
        response = dateutil.parser._parser._timelex.isword(cls, nextchar)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def isnum(cls, nextchar):
    """Auto-generated function: isnum"""
    try:
        response = dateutil.parser._parser._timelex.isnum(cls, nextchar)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def isspace(cls, nextchar):
    """Auto-generated function: isspace"""
    try:
        response = dateutil.parser._parser._timelex.isspace(cls, nextchar)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def jump(name):
    """Auto-generated function: jump"""
    try:
        response = dateutil.parser._parser.parserinfo.jump(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def weekday(name):
    """Auto-generated function: weekday"""
    try:
        response = dateutil.parser._parser.parserinfo.weekday(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def month(name):
    """Auto-generated function: month"""
    try:
        response = dateutil.parser._parser.parserinfo.month(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def hms(name):
    """Auto-generated function: hms"""
    try:
        response = dateutil.parser._parser.parserinfo.hms(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def ampm(name):
    """Auto-generated function: ampm"""
    try:
        response = dateutil.parser._parser.parserinfo.ampm(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def pertain(name):
    """Auto-generated function: pertain"""
    try:
        response = dateutil.parser._parser.parserinfo.pertain(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def utczone(name):
    """Auto-generated function: utczone"""
    try:
        response = dateutil.parser._parser.parserinfo.utczone(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tzoffset(name):
    """Auto-generated function: tzoffset"""
    try:
        response = dateutil.parser._parser.parserinfo.tzoffset(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def convertyear(year, century_specified):
    """Auto-generated function: convertyear"""
    try:
        response = dateutil.parser._parser.parserinfo.convertyear(year, century_specified)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def validate(res):
    """Auto-generated function: validate"""
    try:
        response = dateutil.parser._parser.parserinfo.validate(res)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def has_year():
    """Auto-generated function: has_year"""
    try:
        response = dateutil.parser._parser._ymd.has_year()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def has_month():
    """Auto-generated function: has_month"""
    try:
        response = dateutil.parser._parser._ymd.has_month()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def has_day():
    """Auto-generated function: has_day"""
    try:
        response = dateutil.parser._parser._ymd.has_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def could_be_day(value):
    """Auto-generated function: could_be_day"""
    try:
        response = dateutil.parser._parser._ymd.could_be_day(value)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def append(val, label):
    """Auto-generated function: append"""
    try:
        response = dateutil.parser._parser._ymd.append(val, label)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def resolve_ymd(yearfirst, dayfirst):
    """Auto-generated function: resolve_ymd"""
    try:
        response = dateutil.parser._parser._ymd.resolve_ymd(yearfirst, dayfirst)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def parse(tzstr):
    """Auto-generated function: parse"""
    try:
        response = dateutil.parser._parser._tzparser.parse(tzstr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def rebuild(filename, tag, format, zonegroups, metadata):
    """Auto-generated function: rebuild"""
    try:
        response = dateutil.zoneinfo.rebuild.rebuild(filename, tag, format, zonegroups, metadata)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def getzoneinfofile_stream():
    """Auto-generated function: getzoneinfofile_stream"""
    try:
        response = dateutil.zoneinfo.__init__.getzoneinfofile_stream()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get(name, default):
    """Auto-generated function: get"""
    try:
        response = dateutil.zoneinfo.__init__.ZoneInfoFile.get(name, default)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_zonefile_instance(new_instance):
    """Auto-generated function: get_zonefile_instance"""
    try:
        response = dateutil.zoneinfo.__init__.get_zonefile_instance(new_instance)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def gettz(name):
    """Auto-generated function: gettz"""
    try:
        response = dateutil.zoneinfo.__init__.gettz(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def gettz_db_metadata():
    """Auto-generated function: gettz_db_metadata"""
    try:
        response = dateutil.zoneinfo.__init__.gettz_db_metadata()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInheritance():
    """Auto-generated function: testInheritance"""
    try:
        response = dateutil.RelativeDeltaTest.testInheritance()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthEndMonthBeginning():
    """Auto-generated function: testMonthEndMonthBeginning"""
    try:
        response = dateutil.RelativeDeltaTest.testMonthEndMonthBeginning()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthEndMonthBeginningLeapYear():
    """Auto-generated function: testMonthEndMonthBeginningLeapYear"""
    try:
        response = dateutil.RelativeDeltaTest.testMonthEndMonthBeginningLeapYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextMonth():
    """Auto-generated function: testNextMonth"""
    try:
        response = dateutil.RelativeDeltaTest.testNextMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextMonthPlusOneWeek():
    """Auto-generated function: testNextMonthPlusOneWeek"""
    try:
        response = dateutil.RelativeDeltaTest.testNextMonthPlusOneWeek()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextMonthPlusOneWeek10am():
    """Auto-generated function: testNextMonthPlusOneWeek10am"""
    try:
        response = dateutil.RelativeDeltaTest.testNextMonthPlusOneWeek10am()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextMonthPlusOneWeek10amDiff():
    """Auto-generated function: testNextMonthPlusOneWeek10amDiff"""
    try:
        response = dateutil.RelativeDeltaTest.testNextMonthPlusOneWeek10amDiff()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testOneMonthBeforeOneYear():
    """Auto-generated function: testOneMonthBeforeOneYear"""
    try:
        response = dateutil.RelativeDeltaTest.testOneMonthBeforeOneYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthsOfDiffNumOfDays():
    """Auto-generated function: testMonthsOfDiffNumOfDays"""
    try:
        response = dateutil.RelativeDeltaTest.testMonthsOfDiffNumOfDays()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthsOfDiffNumOfDaysWithYears():
    """Auto-generated function: testMonthsOfDiffNumOfDaysWithYears"""
    try:
        response = dateutil.RelativeDeltaTest.testMonthsOfDiffNumOfDaysWithYears()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextFriday():
    """Auto-generated function: testNextFriday"""
    try:
        response = dateutil.RelativeDeltaTest.testNextFriday()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextFridayInt():
    """Auto-generated function: testNextFridayInt"""
    try:
        response = dateutil.RelativeDeltaTest.testNextFridayInt()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLastFridayInThisMonth():
    """Auto-generated function: testLastFridayInThisMonth"""
    try:
        response = dateutil.RelativeDeltaTest.testLastFridayInThisMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLastDayOfFebruary():
    """Auto-generated function: testLastDayOfFebruary"""
    try:
        response = dateutil.RelativeDeltaTest.testLastDayOfFebruary()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLastDayOfFebruaryLeapYear():
    """Auto-generated function: testLastDayOfFebruaryLeapYear"""
    try:
        response = dateutil.RelativeDeltaTest.testLastDayOfFebruaryLeapYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextWednesdayIsToday():
    """Auto-generated function: testNextWednesdayIsToday"""
    try:
        response = dateutil.RelativeDeltaTest.testNextWednesdayIsToday()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNextWednesdayNotToday():
    """Auto-generated function: testNextWednesdayNotToday"""
    try:
        response = dateutil.RelativeDeltaTest.testNextWednesdayNotToday()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAddMoreThan12Months():
    """Auto-generated function: testAddMoreThan12Months"""
    try:
        response = dateutil.RelativeDeltaTest.testAddMoreThan12Months()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAddNegativeMonths():
    """Auto-generated function: testAddNegativeMonths"""
    try:
        response = dateutil.RelativeDeltaTest.testAddNegativeMonths()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test15thISOYearWeek():
    """Auto-generated function: test15thISOYearWeek"""
    try:
        response = dateutil.RelativeDeltaTest.test15thISOYearWeek()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMillenniumAge():
    """Auto-generated function: testMillenniumAge"""
    try:
        response = dateutil.RelativeDeltaTest.testMillenniumAge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testJohnAge():
    """Auto-generated function: testJohnAge"""
    try:
        response = dateutil.RelativeDeltaTest.testJohnAge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testJohnAgeWithDate():
    """Auto-generated function: testJohnAgeWithDate"""
    try:
        response = dateutil.RelativeDeltaTest.testJohnAgeWithDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearDay():
    """Auto-generated function: testYearDay"""
    try:
        response = dateutil.RelativeDeltaTest.testYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearDayBug():
    """Auto-generated function: testYearDayBug"""
    try:
        response = dateutil.RelativeDeltaTest.testYearDayBug()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNonLeapYearDay():
    """Auto-generated function: testNonLeapYearDay"""
    try:
        response = dateutil.RelativeDeltaTest.testNonLeapYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAddition():
    """Auto-generated function: testAddition"""
    try:
        response = dateutil.RelativeDeltaTest.testAddition()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAbsoluteAddition():
    """Auto-generated function: testAbsoluteAddition"""
    try:
        response = dateutil.RelativeDeltaTest.testAbsoluteAddition()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAdditionToDatetime():
    """Auto-generated function: testAdditionToDatetime"""
    try:
        response = dateutil.RelativeDeltaTest.testAdditionToDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRightAdditionToDatetime():
    """Auto-generated function: testRightAdditionToDatetime"""
    try:
        response = dateutil.RelativeDeltaTest.testRightAdditionToDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAdditionInvalidType():
    """Auto-generated function: testAdditionInvalidType"""
    try:
        response = dateutil.RelativeDeltaTest.testAdditionInvalidType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAdditionUnsupportedType():
    """Auto-generated function: testAdditionUnsupportedType"""
    try:
        response = dateutil.RelativeDeltaTest.testAdditionUnsupportedType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAdditionFloatValue():
    """Auto-generated function: testAdditionFloatValue"""
    try:
        response = dateutil.RelativeDeltaTest.testAdditionFloatValue()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAdditionFloatFractionals():
    """Auto-generated function: testAdditionFloatFractionals"""
    try:
        response = dateutil.RelativeDeltaTest.testAdditionFloatFractionals()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSubtraction():
    """Auto-generated function: testSubtraction"""
    try:
        response = dateutil.RelativeDeltaTest.testSubtraction()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRightSubtractionFromDatetime():
    """Auto-generated function: testRightSubtractionFromDatetime"""
    try:
        response = dateutil.RelativeDeltaTest.testRightSubtractionFromDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSubractionWithDatetime():
    """Auto-generated function: testSubractionWithDatetime"""
    try:
        response = dateutil.RelativeDeltaTest.testSubractionWithDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSubtractionInvalidType():
    """Auto-generated function: testSubtractionInvalidType"""
    try:
        response = dateutil.RelativeDeltaTest.testSubtractionInvalidType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSubtractionUnsupportedType():
    """Auto-generated function: testSubtractionUnsupportedType"""
    try:
        response = dateutil.RelativeDeltaTest.testSubtractionUnsupportedType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiplication():
    """Auto-generated function: testMultiplication"""
    try:
        response = dateutil.RelativeDeltaTest.testMultiplication()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiplicationUnsupportedType():
    """Auto-generated function: testMultiplicationUnsupportedType"""
    try:
        response = dateutil.RelativeDeltaTest.testMultiplicationUnsupportedType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDivision():
    """Auto-generated function: testDivision"""
    try:
        response = dateutil.RelativeDeltaTest.testDivision()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDivisionUnsupportedType():
    """Auto-generated function: testDivisionUnsupportedType"""
    try:
        response = dateutil.RelativeDeltaTest.testDivisionUnsupportedType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBoolean():
    """Auto-generated function: testBoolean"""
    try:
        response = dateutil.RelativeDeltaTest.testBoolean()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAbsoluteValueNegative():
    """Auto-generated function: testAbsoluteValueNegative"""
    try:
        response = dateutil.RelativeDeltaTest.testAbsoluteValueNegative()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAbsoluteValuePositive():
    """Auto-generated function: testAbsoluteValuePositive"""
    try:
        response = dateutil.RelativeDeltaTest.testAbsoluteValuePositive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testComparison():
    """Auto-generated function: testComparison"""
    try:
        response = dateutil.RelativeDeltaTest.testComparison()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityTypeMismatch():
    """Auto-generated function: testInequalityTypeMismatch"""
    try:
        response = dateutil.RelativeDeltaTest.testInequalityTypeMismatch()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityUnsupportedType():
    """Auto-generated function: testInequalityUnsupportedType"""
    try:
        response = dateutil.RelativeDeltaTest.testInequalityUnsupportedType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityWeekdays():
    """Auto-generated function: testInequalityWeekdays"""
    try:
        response = dateutil.RelativeDeltaTest.testInequalityWeekdays()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthOverflow():
    """Auto-generated function: testMonthOverflow"""
    try:
        response = dateutil.RelativeDeltaTest.testMonthOverflow()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeks():
    """Auto-generated function: testWeeks"""
    try:
        response = dateutil.RelativeDeltaTest.testWeeks()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaRepr():
    """Auto-generated function: testRelativeDeltaRepr"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalYear():
    """Auto-generated function: testRelativeDeltaFractionalYear"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalMonth():
    """Auto-generated function: testRelativeDeltaFractionalMonth"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaInvalidDatetimeObject():
    """Auto-generated function: testRelativeDeltaInvalidDatetimeObject"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaInvalidDatetimeObject()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalAbsolutes():
    """Auto-generated function: testRelativeDeltaFractionalAbsolutes"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalAbsolutes()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalRepr():
    """Auto-generated function: testRelativeDeltaFractionalRepr"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalWeeks():
    """Auto-generated function: testRelativeDeltaFractionalWeeks"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalWeeks()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalDays():
    """Auto-generated function: testRelativeDeltaFractionalDays"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalDays()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalHours():
    """Auto-generated function: testRelativeDeltaFractionalHours"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalHours()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalMinutes():
    """Auto-generated function: testRelativeDeltaFractionalMinutes"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalMinutes()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalSeconds():
    """Auto-generated function: testRelativeDeltaFractionalSeconds"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalSeconds()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalPositiveOverflow():
    """Auto-generated function: testRelativeDeltaFractionalPositiveOverflow"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalPositiveOverflow()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalNegativeDays():
    """Auto-generated function: testRelativeDeltaFractionalNegativeDays"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalNegativeDays()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaNormalizeFractionalDays():
    """Auto-generated function: testRelativeDeltaNormalizeFractionalDays"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaNormalizeFractionalDays()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaNormalizeFractionalDays2():
    """Auto-generated function: testRelativeDeltaNormalizeFractionalDays2"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaNormalizeFractionalDays2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaNormalizeFractionalMinutes():
    """Auto-generated function: testRelativeDeltaNormalizeFractionalMinutes"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaNormalizeFractionalMinutes()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaNormalizeFractionalSeconds():
    """Auto-generated function: testRelativeDeltaNormalizeFractionalSeconds"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaNormalizeFractionalSeconds()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalPositiveOverflow2():
    """Auto-generated function: testRelativeDeltaFractionalPositiveOverflow2"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalPositiveOverflow2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRelativeDeltaFractionalNegativeOverflow():
    """Auto-generated function: testRelativeDeltaFractionalNegativeOverflow"""
    try:
        response = dateutil.RelativeDeltaTest.testRelativeDeltaFractionalNegativeOverflow()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInvalidYearDay():
    """Auto-generated function: testInvalidYearDay"""
    try:
        response = dateutil.RelativeDeltaTest.testInvalidYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAddTimedeltaToUnpopulatedRelativedelta():
    """Auto-generated function: testAddTimedeltaToUnpopulatedRelativedelta"""
    try:
        response = dateutil.RelativeDeltaTest.testAddTimedeltaToUnpopulatedRelativedelta()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAddTimedeltaToPopulatedRelativeDelta():
    """Auto-generated function: testAddTimedeltaToPopulatedRelativeDelta"""
    try:
        response = dateutil.RelativeDeltaTest.testAddTimedeltaToPopulatedRelativeDelta()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHashable():
    """Auto-generated function: testHashable"""
    try:
        response = dateutil.RelativeDeltaTest.testHashable()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDayOfMonthPlus():
    """Auto-generated function: testDayOfMonthPlus"""
    try:
        response = dateutil.RelativeDeltaTest.testDayOfMonthPlus()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLastDayOfMonthPlus():
    """Auto-generated function: testLastDayOfMonthPlus"""
    try:
        response = dateutil.RelativeDeltaTest.testLastDayOfMonthPlus()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDayOfMonthMinus():
    """Auto-generated function: testDayOfMonthMinus"""
    try:
        response = dateutil.RelativeDeltaTest.testDayOfMonthMinus()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLastDayOfMonthMinus():
    """Auto-generated function: testLastDayOfMonthMinus"""
    try:
        response = dateutil.RelativeDeltaTest.testLastDayOfMonthMinus()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_one_day():
    """Auto-generated function: test_one_day"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertyGetterTest.test_one_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_minus_one_day():
    """Auto-generated function: test_minus_one_day"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertyGetterTest.test_minus_one_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_height_days():
    """Auto-generated function: test_height_days"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertyGetterTest.test_height_days()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_minus_height_days():
    """Auto-generated function: test_minus_height_days"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertyGetterTest.test_minus_height_days()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_one_day_set_one_week():
    """Auto-generated function: test_one_day_set_one_week"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertySetterTest.test_one_day_set_one_week()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_minus_one_day_set_one_week():
    """Auto-generated function: test_minus_one_day_set_one_week"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertySetterTest.test_minus_one_day_set_one_week()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_height_days_set_minus_one_week():
    """Auto-generated function: test_height_days_set_minus_one_week"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertySetterTest.test_height_days_set_minus_one_week()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_minus_height_days_set_minus_one_week():
    """Auto-generated function: test_minus_height_days_set_minus_one_week"""
    try:
        response = dateutil.RelativeDeltaWeeksPropertySetterTest.test_minus_height_days_set_minus_one_week()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def pytest_collection_modifyitems(items):
    """Auto-generated function: pytest_collection_modifyitems"""
    try:
        response = dateutil.pytest_collection_modifyitems(items)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def set_tzpath():
    """Auto-generated function: set_tzpath"""
    try:
        response = dateutil.set_tzpath()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_imported_modules():
    """Auto-generated function: test_imported_modules"""
    try:
        response = dateutil.test_imported_modules()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_easter_western(easter_date):
    """Auto-generated function: test_easter_western"""
    try:
        response = dateutil.test_easter_western(easter_date)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_easter_orthodox(easter_date):
    """Auto-generated function: test_easter_orthodox"""
    try:
        response = dateutil.test_easter_orthodox(easter_date)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_easter_julian(easter_date):
    """Auto-generated function: test_easter_julian"""
    try:
        response = dateutil.test_easter_julian(easter_date)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_easter_bad_method():
    """Auto-generated function: test_easter_bad_method"""
    try:
        response = dateutil.test_easter_bad_method()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_timezone_tuple(dt):
    """Auto-generated function: get_timezone_tuple"""
    try:
        response = dateutil.get_timezone_tuple(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def gettz(tzname):
    """Auto-generated function: gettz"""
    try:
        response = dateutil.TZICalTest.gettz(tzname)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFoldPositiveUTCOffset():
    """Auto-generated function: testFoldPositiveUTCOffset"""
    try:
        response = dateutil.TzWinFoldMixin.testFoldPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGapPositiveUTCOffset():
    """Auto-generated function: testGapPositiveUTCOffset"""
    try:
        response = dateutil.TzWinFoldMixin.testGapPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFoldNegativeUTCOffset():
    """Auto-generated function: testFoldNegativeUTCOffset"""
    try:
        response = dateutil.TzWinFoldMixin.testFoldNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGapNegativeUTCOffset():
    """Auto-generated function: testGapNegativeUTCOffset"""
    try:
        response = dateutil.TzWinFoldMixin.testGapNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFoldLondon():
    """Auto-generated function: testFoldLondon"""
    try:
        response = dateutil.TzFoldMixin.testFoldLondon()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFoldIndependence():
    """Auto-generated function: testFoldIndependence"""
    try:
        response = dateutil.TzWinFoldMixin.testFoldIndependence()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInZoneFoldEquality():
    """Auto-generated function: testInZoneFoldEquality"""
    try:
        response = dateutil.TzWinFoldMixin.testInZoneFoldEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAmbiguousNegativeUTCOffset():
    """Auto-generated function: testAmbiguousNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testAmbiguousNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAmbiguousPositiveUTCOffset():
    """Auto-generated function: testAmbiguousPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testAmbiguousPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousNegativeUTCOffset():
    """Auto-generated function: testUnambiguousNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testUnambiguousNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousPositiveUTCOffset():
    """Auto-generated function: testUnambiguousPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testUnambiguousPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousGapNegativeUTCOffset():
    """Auto-generated function: testUnambiguousGapNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testUnambiguousGapNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousGapPositiveUTCOffset():
    """Auto-generated function: testUnambiguousGapPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testUnambiguousGapPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testImaginaryNegativeUTCOffset():
    """Auto-generated function: testImaginaryNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testImaginaryNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNotImaginaryNegativeUTCOffset():
    """Auto-generated function: testNotImaginaryNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testNotImaginaryNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testImaginaryPositiveUTCOffset():
    """Auto-generated function: testImaginaryPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testImaginaryPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNotImaginaryPositiveUTCOffset():
    """Auto-generated function: testNotImaginaryPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testNotImaginaryPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNotImaginaryFoldNegativeUTCOffset():
    """Auto-generated function: testNotImaginaryFoldNegativeUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testNotImaginaryFoldNegativeUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNotImaginaryFoldPositiveUTCOffset():
    """Auto-generated function: testNotImaginaryFoldPositiveUTCOffset"""
    try:
        response = dateutil.TzFoldMixin.testNotImaginaryFoldPositiveUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testEqualAmbiguousComparison():
    """Auto-generated function: testEqualAmbiguousComparison"""
    try:
        response = dateutil.TzFoldMixin.testEqualAmbiguousComparison()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_args(tzname):
    """Auto-generated function: get_args"""
    try:
        response = dateutil.TzWinLocalTest.get_args(tzname)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_utc_transitions(tzi, year, gap):
    """Auto-generated function: get_utc_transitions"""
    try:
        response = dateutil.TzWinFoldMixin.get_utc_transitions(tzi, year, gap)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSingleton():
    """Auto-generated function: testSingleton"""
    try:
        response = dateutil.TzUTCTest.testSingleton()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testOffset():
    """Auto-generated function: testOffset"""
    try:
        response = dateutil.TzWinTest.testOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDst():
    """Auto-generated function: testDst"""
    try:
        response = dateutil.TzUTCTest.testDst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzName():
    """Auto-generated function: testTzName"""
    try:
        response = dateutil.TzUTCTest.testTzName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testEquality():
    """Auto-generated function: testEquality"""
    try:
        response = dateutil.TzLocalTest.testEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequality():
    """Auto-generated function: testInequality"""
    try:
        response = dateutil.TzUTCTest.testInequality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityInteger():
    """Auto-generated function: testInequalityInteger"""
    try:
        response = dateutil.TzUTCTest.testInequalityInteger()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityUnsupported():
    """Auto-generated function: testInequalityUnsupported"""
    try:
        response = dateutil.TzLocalTest.testInequalityUnsupported()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRepr():
    """Auto-generated function: testRepr"""
    try:
        response = dateutil.TZICalTest.testRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyUTC():
    """Auto-generated function: testTimeOnlyUTC"""
    try:
        response = dateutil.TzUTCTest.testTimeOnlyUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAmbiguity():
    """Auto-generated function: testAmbiguity"""
    try:
        response = dateutil.TzOffsetTest.testAmbiguity()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimedeltaOffset():
    """Auto-generated function: testTimedeltaOffset"""
    try:
        response = dateutil.TzOffsetTest.testTimedeltaOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzNameNone():
    """Auto-generated function: testTzNameNone"""
    try:
        response = dateutil.TzOffsetTest.testTzNameNone()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyOffset():
    """Auto-generated function: testTimeOnlyOffset"""
    try:
        response = dateutil.TzOffsetTest.testTimeOnlyOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzOffsetRepr():
    """Auto-generated function: testTzOffsetRepr"""
    try:
        response = dateutil.TzOffsetTest.testTzOffsetRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUTCEquality():
    """Auto-generated function: testUTCEquality"""
    try:
        response = dateutil.TzLocalNixTest.testUTCEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityInvalid():
    """Auto-generated function: testInequalityInvalid"""
    try:
        response = dateutil.TzLocalTest.testInequalityInvalid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzOffsetInstance():
    """Auto-generated function: testTzOffsetInstance"""
    try:
        response = dateutil.TzOffsetTest.testTzOffsetInstance()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzOffsetSingletonDifferent():
    """Auto-generated function: testTzOffsetSingletonDifferent"""
    try:
        response = dateutil.TzOffsetTest.testTzOffsetSingletonDifferent()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_weakref():
    """Auto-generated function: test_tzoffset_weakref"""
    try:
        response = dateutil.test_tzoffset_weakref()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_singleton(args):
    """Auto-generated function: test_tzoffset_singleton"""
    try:
        response = dateutil.test_tzoffset_singleton(args)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_sub_minute():
    """Auto-generated function: test_tzoffset_sub_minute"""
    try:
        response = dateutil.test_tzoffset_sub_minute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_sub_minute_rounding():
    """Auto-generated function: test_tzoffset_sub_minute_rounding"""
    try:
        response = dateutil.test_tzoffset_sub_minute_rounding()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInequalityFixedOffset():
    """Auto-generated function: testInequalityFixedOffset"""
    try:
        response = dateutil.TzLocalTest.testInequalityFixedOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_is(args, kwargs):
    """Auto-generated function: test_tzoffset_is"""
    try:
        response = dateutil.test_tzoffset_is(args, kwargs)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzoffset_is_not():
    """Auto-generated function: test_tzoffset_is_not"""
    try:
        response = dateutil.test_tzoffset_is_not()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzNameDST():
    """Auto-generated function: testTzNameDST"""
    try:
        response = dateutil.TzLocalNixTest.testTzNameDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzNameUTC():
    """Auto-generated function: testTzNameUTC"""
    try:
        response = dateutil.TzLocalNixTest.testTzNameUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testOffsetDST():
    """Auto-generated function: testOffsetDST"""
    try:
        response = dateutil.TzLocalNixTest.testOffsetDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testOffsetUTC():
    """Auto-generated function: testOffsetUTC"""
    try:
        response = dateutil.TzLocalNixTest.testOffsetUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDSTDST():
    """Auto-generated function: testDSTDST"""
    try:
        response = dateutil.TzLocalNixTest.testDSTDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDSTUTC():
    """Auto-generated function: testDSTUTC"""
    try:
        response = dateutil.TzLocalNixTest.testDSTUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyOffsetLocalUTC():
    """Auto-generated function: testTimeOnlyOffsetLocalUTC"""
    try:
        response = dateutil.TzLocalNixTest.testTimeOnlyOffsetLocalUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyOffsetLocalDST():
    """Auto-generated function: testTimeOnlyOffsetLocalDST"""
    try:
        response = dateutil.TzLocalNixTest.testTimeOnlyOffsetLocalDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyDSTLocalUTC():
    """Auto-generated function: testTimeOnlyDSTLocalUTC"""
    try:
        response = dateutil.TzLocalNixTest.testTimeOnlyDSTLocalUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyDSTLocalDST():
    """Auto-generated function: testTimeOnlyDSTLocalDST"""
    try:
        response = dateutil.TzLocalNixTest.testTimeOnlyDSTLocalDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mark_tzlocal_nix(f):
    """Auto-generated function: mark_tzlocal_nix"""
    try:
        response = dateutil.mark_tzlocal_nix(f)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_utc_equal(tzvar):
    """Auto-generated function: test_tzlocal_utc_equal"""
    try:
        response = dateutil.test_tzlocal_utc_equal(tzvar)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_utc_unequal(tzvar):
    """Auto-generated function: test_tzlocal_utc_unequal"""
    try:
        response = dateutil.test_tzlocal_utc_unequal(tzvar)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_local_time_trim_colon():
    """Auto-generated function: test_tzlocal_local_time_trim_colon"""
    try:
        response = dateutil.test_tzlocal_local_time_trim_colon()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_offset_equal(tzvar, tzoff):
    """Auto-generated function: test_tzlocal_offset_equal"""
    try:
        response = dateutil.test_tzlocal_offset_equal(tzvar, tzoff)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_offset_unequal(tzvar, tzoff):
    """Auto-generated function: test_tzlocal_offset_unequal"""
    try:
        response = dateutil.test_tzlocal_offset_unequal(tzvar, tzoff)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGettz():
    """Auto-generated function: testGettz"""
    try:
        response = dateutil.GettzTest.testGettz()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetTzEquality():
    """Auto-generated function: testGetTzEquality"""
    try:
        response = dateutil.GettzTest.testGetTzEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyGettz():
    """Auto-generated function: testTimeOnlyGettz"""
    try:
        response = dateutil.GettzTest.testTimeOnlyGettz()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyGettzDST():
    """Auto-generated function: testTimeOnlyGettzDST"""
    try:
        response = dateutil.GettzTest.testTimeOnlyGettzDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyGettzTzName():
    """Auto-generated function: testTimeOnlyGettzTzName"""
    try:
        response = dateutil.GettzTest.testTimeOnlyGettzTzName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyFormatZ():
    """Auto-generated function: testTimeOnlyFormatZ"""
    try:
        response = dateutil.GettzTest.testTimeOnlyFormatZ()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPortugalDST():
    """Auto-generated function: testPortugalDST"""
    try:
        response = dateutil.GettzTest.testPortugalDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGettzCacheTzFile():
    """Auto-generated function: testGettzCacheTzFile"""
    try:
        response = dateutil.GettzTest.testGettzCacheTzFile()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGettzCacheTzLocal():
    """Auto-generated function: testGettzCacheTzLocal"""
    try:
        response = dateutil.GettzTest.testGettzCacheTzLocal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_same_result_for_none_and_empty_string():
    """Auto-generated function: test_gettz_same_result_for_none_and_empty_string"""
    try:
        response = dateutil.test_gettz_same_result_for_none_and_empty_string()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_badzone(badzone):
    """Auto-generated function: test_gettz_badzone"""
    try:
        response = dateutil.test_gettz_badzone(badzone)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_badzone_unicode():
    """Auto-generated function: test_gettz_badzone_unicode"""
    try:
        response = dateutil.test_gettz_badzone_unicode()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_zone_wrong_type(badzone, exc_reason):
    """Auto-generated function: test_gettz_zone_wrong_type"""
    try:
        response = dateutil.test_gettz_zone_wrong_type(badzone, exc_reason)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_cache_clear():
    """Auto-generated function: test_gettz_cache_clear"""
    try:
        response = dateutil.test_gettz_cache_clear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_set_cache_size():
    """Auto-generated function: test_gettz_set_cache_size"""
    try:
        response = dateutil.test_gettz_set_cache_size()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_weakref():
    """Auto-generated function: test_gettz_weakref"""
    try:
        response = dateutil.test_gettz_weakref()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoFileStart1():
    """Auto-generated function: testZoneInfoFileStart1"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoFileStart1()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoFileEnd1():
    """Auto-generated function: testZoneInfoFileEnd1"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoFileEnd1()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoOffsetSignal():
    """Auto-generated function: testZoneInfoOffsetSignal"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoOffsetSignal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoCopy():
    """Auto-generated function: testZoneInfoCopy"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoCopy()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoDeepCopy():
    """Auto-generated function: testZoneInfoDeepCopy"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoDeepCopy()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoInstanceCaching():
    """Auto-generated function: testZoneInfoInstanceCaching"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoInstanceCaching()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoNewInstance():
    """Auto-generated function: testZoneInfoNewInstance"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoNewInstance()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoDeprecated():
    """Auto-generated function: testZoneInfoDeprecated"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoDeprecated()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testZoneInfoMetadataDeprecated():
    """Auto-generated function: testZoneInfoMetadataDeprecated"""
    try:
        response = dateutil.ZoneInfoGettzTest.testZoneInfoMetadataDeprecated()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeCmp1():
    """Auto-generated function: testRangeCmp1"""
    try:
        response = dateutil.TZRangeTest.testRangeCmp1()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeCmp2():
    """Auto-generated function: testRangeCmp2"""
    try:
        response = dateutil.TZRangeTest.testRangeCmp2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeOffsets():
    """Auto-generated function: testRangeOffsets"""
    try:
        response = dateutil.TZRangeTest.testRangeOffsets()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyRangeFixed():
    """Auto-generated function: testTimeOnlyRangeFixed"""
    try:
        response = dateutil.TZRangeTest.testTimeOnlyRangeFixed()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTimeOnlyRange():
    """Auto-generated function: testTimeOnlyRange"""
    try:
        response = dateutil.TZRangeTest.testTimeOnlyRange()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBrokenIsDstHandling():
    """Auto-generated function: testBrokenIsDstHandling"""
    try:
        response = dateutil.TZRangeTest.testBrokenIsDstHandling()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeTimeDelta():
    """Auto-generated function: testRangeTimeDelta"""
    try:
        response = dateutil.TZRangeTest.testRangeTimeDelta()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeEquality():
    """Auto-generated function: testRangeEquality"""
    try:
        response = dateutil.TZRangeTest.testRangeEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRangeInequalityUnsupported():
    """Auto-generated function: testRangeInequalityUnsupported"""
    try:
        response = dateutil.TZRangeTest.testRangeInequalityUnsupported()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrStr():
    """Auto-generated function: testStrStr"""
    try:
        response = dateutil.TZStrTest.testStrStr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrInequality():
    """Auto-generated function: testStrInequality"""
    try:
        response = dateutil.TZStrTest.testStrInequality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrInequalityStartEnd():
    """Auto-generated function: testStrInequalityStartEnd"""
    try:
        response = dateutil.TZStrTest.testStrInequalityStartEnd()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPosixOffset():
    """Auto-generated function: testPosixOffset"""
    try:
        response = dateutil.TZStrTest.testPosixOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrInequalityUnsupported():
    """Auto-generated function: testStrInequalityUnsupported"""
    try:
        response = dateutil.TZStrTest.testStrInequalityUnsupported()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzStrRepr():
    """Auto-generated function: testTzStrRepr"""
    try:
        response = dateutil.TZStrTest.testTzStrRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzStrFailure():
    """Auto-generated function: testTzStrFailure"""
    try:
        response = dateutil.TZStrTest.testTzStrFailure()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzStrSingleton():
    """Auto-generated function: testTzStrSingleton"""
    try:
        response = dateutil.TZStrTest.testTzStrSingleton()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzStrSingletonPosix():
    """Auto-generated function: testTzStrSingletonPosix"""
    try:
        response = dateutil.TZStrTest.testTzStrSingletonPosix()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzStrInstance():
    """Auto-generated function: testTzStrInstance"""
    try:
        response = dateutil.TZStrTest.testTzStrInstance()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzstr_weakref():
    """Auto-generated function: test_tzstr_weakref"""
    try:
        response = dateutil.test_tzstr_weakref()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_GNU_tzstr(tz_str, expected):
    """Auto-generated function: test_valid_GNU_tzstr"""
    try:
        response = dateutil.test_valid_GNU_tzstr(tz_str, expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_dateutil_format(tz_str, expected):
    """Auto-generated function: test_valid_dateutil_format"""
    try:
        response = dateutil.test_valid_dateutil_format(tz_str, expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_invalid_GNU_tzstr(tz_str):
    """Auto-generated function: test_invalid_GNU_tzstr"""
    try:
        response = dateutil.test_invalid_GNU_tzstr(tz_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzstr_default_start(tz_str):
    """Auto-generated function: test_tzstr_default_start"""
    try:
        response = dateutil.test_tzstr_default_start(tz_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzstr_default_end(tz_str):
    """Auto-generated function: test_tzstr_default_end"""
    try:
        response = dateutil.test_tzstr_default_end(tz_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzstr_default_cmp(tzstr_1, tzstr_2):
    """Auto-generated function: test_tzstr_default_cmp"""
    try:
        response = dateutil.test_tzstr_default_cmp(tzstr_1, tzstr_2)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTStartName():
    """Auto-generated function: testESTStartName"""
    try:
        response = dateutil.TZICalTest.testESTStartName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTEndName():
    """Auto-generated function: testESTEndName"""
    try:
        response = dateutil.TZICalTest.testESTEndName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTStartOffset():
    """Auto-generated function: testESTStartOffset"""
    try:
        response = dateutil.TZICalTest.testESTStartOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTEndOffset():
    """Auto-generated function: testESTEndOffset"""
    try:
        response = dateutil.TZICalTest.testESTEndOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTStartDST():
    """Auto-generated function: testESTStartDST"""
    try:
        response = dateutil.TZICalTest.testESTStartDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTEndDST():
    """Auto-generated function: testESTEndDST"""
    try:
        response = dateutil.TZICalTest.testESTEndDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testESTValueDatetime():
    """Auto-generated function: testESTValueDatetime"""
    try:
        response = dateutil.TZICalTest.testESTValueDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneStartName():
    """Auto-generated function: testMultiZoneStartName"""
    try:
        response = dateutil.TZICalTest.testMultiZoneStartName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneEndName():
    """Auto-generated function: testMultiZoneEndName"""
    try:
        response = dateutil.TZICalTest.testMultiZoneEndName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneStartOffset():
    """Auto-generated function: testMultiZoneStartOffset"""
    try:
        response = dateutil.TZICalTest.testMultiZoneStartOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneEndOffset():
    """Auto-generated function: testMultiZoneEndOffset"""
    try:
        response = dateutil.TZICalTest.testMultiZoneEndOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneStartDST():
    """Auto-generated function: testMultiZoneStartDST"""
    try:
        response = dateutil.TZICalTest.testMultiZoneStartDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneEndDST():
    """Auto-generated function: testMultiZoneEndDST"""
    try:
        response = dateutil.TZICalTest.testMultiZoneEndDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneKeys():
    """Auto-generated function: testMultiZoneKeys"""
    try:
        response = dateutil.TZICalTest.testMultiZoneKeys()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testEmptyString():
    """Auto-generated function: testEmptyString"""
    try:
        response = dateutil.TZICalTest.testEmptyString()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMultiZoneGet():
    """Auto-generated function: testMultiZoneGet"""
    try:
        response = dateutil.TZICalTest.testMultiZoneGet()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDtstartDate():
    """Auto-generated function: testDtstartDate"""
    try:
        response = dateutil.TZICalTest.testDtstartDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDtstartTzid():
    """Auto-generated function: testDtstartTzid"""
    try:
        response = dateutil.TZICalTest.testDtstartTzid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDtstartBadParam():
    """Auto-generated function: testDtstartBadParam"""
    try:
        response = dateutil.TZICalTest.testDtstartBadParam()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGap():
    """Auto-generated function: testGap"""
    try:
        response = dateutil.TZICalTest.testGap()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFileStart1():
    """Auto-generated function: testFileStart1"""
    try:
        response = dateutil.TZTest.testFileStart1()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFileEnd1():
    """Auto-generated function: testFileEnd1"""
    try:
        response = dateutil.TZTest.testFileEnd1()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFileLastTransition():
    """Auto-generated function: testFileLastTransition"""
    try:
        response = dateutil.TZTest.testFileLastTransition()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInvalidFile():
    """Auto-generated function: testInvalidFile"""
    try:
        response = dateutil.TZTest.testInvalidFile()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFilestreamWithNameRepr():
    """Auto-generated function: testFilestreamWithNameRepr"""
    try:
        response = dateutil.TZTest.testFilestreamWithNameRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLeapCountDecodesProperly():
    """Auto-generated function: testLeapCountDecodesProperly"""
    try:
        response = dateutil.TZTest.testLeapCountDecodesProperly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIsStd():
    """Auto-generated function: testIsStd"""
    try:
        response = dateutil.TZTest.testIsStd()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGMTHasNoDaylight():
    """Auto-generated function: testGMTHasNoDaylight"""
    try:
        response = dateutil.TZTest.testGMTHasNoDaylight()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGMTOffset():
    """Auto-generated function: testGMTOffset"""
    try:
        response = dateutil.TZTest.testGMTOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTZSetDoesntCorrupt():
    """Auto-generated function: testTZSetDoesntCorrupt"""
    try:
        response = dateutil.TZTest.testTZSetDoesntCorrupt()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzfile_sub_minute_offset():
    """Auto-generated function: test_tzfile_sub_minute_offset"""
    try:
        response = dateutil.test_tzfile_sub_minute_offset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_sub_minute_rounding_tzfile():
    """Auto-generated function: test_sub_minute_rounding_tzfile"""
    try:
        response = dateutil.test_sub_minute_rounding_tzfile()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_samoa_transition():
    """Auto-generated function: test_samoa_transition"""
    try:
        response = dateutil.test_samoa_transition()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def setUp():
    """Auto-generated function: setUp"""
    try:
        response = dateutil.TzPickleTest.setUp()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzResLoadName():
    """Auto-generated function: testTzResLoadName"""
    try:
        response = dateutil.TzWinTest.testTzResLoadName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzResNameFromString():
    """Auto-generated function: testTzResNameFromString"""
    try:
        response = dateutil.TzWinTest.testTzResNameFromString()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIsdstZoneWithNoDaylightSaving():
    """Auto-generated function: testIsdstZoneWithNoDaylightSaving"""
    try:
        response = dateutil.TzWinTest.testIsdstZoneWithNoDaylightSaving()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinName():
    """Auto-generated function: testTzwinName"""
    try:
        response = dateutil.TzWinTest.testTzwinName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinRepr():
    """Auto-generated function: testTzwinRepr"""
    try:
        response = dateutil.TzWinTest.testTzwinRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzWinEquality():
    """Auto-generated function: testTzWinEquality"""
    try:
        response = dateutil.TzWinTest.testTzWinEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzWinInequality():
    """Auto-generated function: testTzWinInequality"""
    try:
        response = dateutil.TzWinTest.testTzWinInequality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzWinEqualityInvalid():
    """Auto-generated function: testTzWinEqualityInvalid"""
    try:
        response = dateutil.TzWinTest.testTzWinEqualityInvalid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzWinInequalityUnsupported():
    """Auto-generated function: testTzWinInequalityUnsupported"""
    try:
        response = dateutil.TzWinTest.testTzWinInequalityUnsupported()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinTimeOnlyDST():
    """Auto-generated function: testTzwinTimeOnlyDST"""
    try:
        response = dateutil.TzWinTest.testTzwinTimeOnlyDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinTimeOnlyUTCOffset():
    """Auto-generated function: testTzwinTimeOnlyUTCOffset"""
    try:
        response = dateutil.TzWinTest.testTzwinTimeOnlyUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinTimeOnlyTZName():
    """Auto-generated function: testTzwinTimeOnlyTZName"""
    try:
        response = dateutil.TzWinTest.testTzwinTimeOnlyTZName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLocal():
    """Auto-generated function: testLocal"""
    try:
        response = dateutil.TzWinLocalTest.testLocal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalUTCOffset():
    """Auto-generated function: testTzwinLocalUTCOffset"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalName():
    """Auto-generated function: testTzwinLocalName"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzWinLocalRepr():
    """Auto-generated function: testTzWinLocalRepr"""
    try:
        response = dateutil.TzWinLocalTest.testTzWinLocalRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalRepr():
    """Auto-generated function: testTzwinLocalRepr"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalRepr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalEquality():
    """Auto-generated function: testTzwinLocalEquality"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalTimeOnlyDST():
    """Auto-generated function: testTzwinLocalTimeOnlyDST"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalTimeOnlyDST()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalTimeOnlyUTCOffset():
    """Auto-generated function: testTzwinLocalTimeOnlyUTCOffset"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalTimeOnlyUTCOffset()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testTzwinLocalTimeOnlyTZName():
    """Auto-generated function: testTzwinLocalTimeOnlyTZName"""
    try:
        response = dateutil.TzWinLocalTest.testTzwinLocalTimeOnlyTZName()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzUTC():
    """Auto-generated function: testPickleTzUTC"""
    try:
        response = dateutil.TzPickleTest.testPickleTzUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzOffsetZero():
    """Auto-generated function: testPickleTzOffsetZero"""
    try:
        response = dateutil.TzPickleTest.testPickleTzOffsetZero()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzOffsetPos():
    """Auto-generated function: testPickleTzOffsetPos"""
    try:
        response = dateutil.TzPickleTest.testPickleTzOffsetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzOffsetNeg():
    """Auto-generated function: testPickleTzOffsetNeg"""
    try:
        response = dateutil.TzPickleTest.testPickleTzOffsetNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzLocal():
    """Auto-generated function: testPickleTzLocal"""
    try:
        response = dateutil.TzPickleTest.testPickleTzLocal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzFileEST5EDT():
    """Auto-generated function: testPickleTzFileEST5EDT"""
    try:
        response = dateutil.TzPickleTest.testPickleTzFileEST5EDT()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzFileEurope_Helsinki():
    """Auto-generated function: testPickleTzFileEurope_Helsinki"""
    try:
        response = dateutil.TzPickleTest.testPickleTzFileEurope_Helsinki()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzFileNew_York():
    """Auto-generated function: testPickleTzFileNew_York"""
    try:
        response = dateutil.TzPickleTest.testPickleTzFileNew_York()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzICal():
    """Auto-generated function: testPickleTzICal"""
    try:
        response = dateutil.TzPickleTest.testPickleTzICal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleTzGettz():
    """Auto-generated function: testPickleTzGettz"""
    try:
        response = dateutil.TzPickleTest.testPickleTzGettz()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPickleZoneFileGettz():
    """Auto-generated function: testPickleZoneFileGettz"""
    try:
        response = dateutil.TzPickleTest.testPickleZoneFileGettz()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoTzSpecified():
    """Auto-generated function: testNoTzSpecified"""
    try:
        response = dateutil.DatetimeExistsTest.testNoTzSpecified()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityFoldNaive():
    """Auto-generated function: testNoSupportAmbiguityFoldNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityFoldNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityFoldAware():
    """Auto-generated function: testNoSupportAmbiguityFoldAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityFoldAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityUnambiguousNaive():
    """Auto-generated function: testNoSupportAmbiguityUnambiguousNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityUnambiguousNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityUnambiguousAware():
    """Auto-generated function: testNoSupportAmbiguityUnambiguousAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityUnambiguousAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityFoldDSTOnly():
    """Auto-generated function: testNoSupportAmbiguityFoldDSTOnly"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityFoldDSTOnly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoSupportAmbiguityUnambiguousDSTOnly():
    """Auto-generated function: testNoSupportAmbiguityUnambiguousDSTOnly"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testNoSupportAmbiguityUnambiguousDSTOnly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSupportAmbiguityFoldNaive():
    """Auto-generated function: testSupportAmbiguityFoldNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testSupportAmbiguityFoldNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSupportAmbiguityFoldAware():
    """Auto-generated function: testSupportAmbiguityFoldAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testSupportAmbiguityFoldAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSupportAmbiguityUnambiguousAware():
    """Auto-generated function: testSupportAmbiguityUnambiguousAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testSupportAmbiguityUnambiguousAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSupportAmbiguityUnambiguousNaive():
    """Auto-generated function: testSupportAmbiguityUnambiguousNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testSupportAmbiguityUnambiguousNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityFoldNaive():
    """Auto-generated function: testIncompatibleAmbiguityFoldNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityFoldNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityFoldAware():
    """Auto-generated function: testIncompatibleAmbiguityFoldAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityFoldAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityUnambiguousNaive():
    """Auto-generated function: testIncompatibleAmbiguityUnambiguousNaive"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityUnambiguousNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityUnambiguousAware():
    """Auto-generated function: testIncompatibleAmbiguityUnambiguousAware"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityUnambiguousAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityFoldDSTOnly():
    """Auto-generated function: testIncompatibleAmbiguityFoldDSTOnly"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityFoldDSTOnly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncompatibleAmbiguityUnambiguousDSTOnly():
    """Auto-generated function: testIncompatibleAmbiguityUnambiguousDSTOnly"""
    try:
        response = dateutil.DatetimeAmbiguousTest.testIncompatibleAmbiguityUnambiguousDSTOnly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSpecifiedTzOverridesAttached():
    """Auto-generated function: testSpecifiedTzOverridesAttached"""
    try:
        response = dateutil.DatetimeExistsTest.testSpecifiedTzOverridesAttached()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInGapNaive():
    """Auto-generated function: testInGapNaive"""
    try:
        response = dateutil.DatetimeExistsTest.testInGapNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInGapAware():
    """Auto-generated function: testInGapAware"""
    try:
        response = dateutil.DatetimeExistsTest.testInGapAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testExistsNaive():
    """Auto-generated function: testExistsNaive"""
    try:
        response = dateutil.DatetimeExistsTest.testExistsNaive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testExistsAware():
    """Auto-generated function: testExistsAware"""
    try:
        response = dateutil.DatetimeExistsTest.testExistsAware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_enter_fold_default():
    """Auto-generated function: test_enter_fold_default"""
    try:
        response = dateutil.TestEnfold.test_enter_fold_default()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_enter_fold():
    """Auto-generated function: test_enter_fold"""
    try:
        response = dateutil.TestEnfold.test_enter_fold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_exit_fold():
    """Auto-generated function: test_exit_fold"""
    try:
        response = dateutil.TestEnfold.test_exit_fold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_defold():
    """Auto-generated function: test_defold"""
    try:
        response = dateutil.TestEnfold.test_defold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_fold_replace_args():
    """Auto-generated function: test_fold_replace_args"""
    try:
        response = dateutil.TestEnfold.test_fold_replace_args()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_fold_replace_exception_duplicate_args():
    """Auto-generated function: test_fold_replace_exception_duplicate_args"""
    try:
        response = dateutil.TestEnfold.test_fold_replace_exception_duplicate_args()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCanberraForward():
    """Auto-generated function: testCanberraForward"""
    try:
        response = dateutil.ImaginaryDateTest.testCanberraForward()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLondonForward():
    """Auto-generated function: testLondonForward"""
    try:
        response = dateutil.ImaginaryDateTest.testLondonForward()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testKeivForward():
    """Auto-generated function: testKeivForward"""
    try:
        response = dateutil.ImaginaryDateTest.testKeivForward()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_resolve_imaginary_ambiguous(dt):
    """Auto-generated function: test_resolve_imaginary_ambiguous"""
    try:
        response = dateutil.test_resolve_imaginary_ambiguous(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_resolve_imaginary_existing(dt):
    """Auto-generated function: test_resolve_imaginary_existing"""
    try:
        response = dateutil.test_resolve_imaginary_existing(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_resolve_imaginary(tzi, dt, dt_exp):
    """Auto-generated function: test_resolve_imaginary"""
    try:
        response = dateutil.test_resolve_imaginary(tzi, dt, dt_exp)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_today():
    """Auto-generated function: test_utils_today"""
    try:
        response = dateutil.test_utils_today()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_today_tz_info():
    """Auto-generated function: test_utils_today_tz_info"""
    try:
        response = dateutil.test_utils_today_tz_info()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_today_tz_info_different_day():
    """Auto-generated function: test_utils_today_tz_info_different_day"""
    try:
        response = dateutil.test_utils_today_tz_info_different_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_default_tz_info_naive():
    """Auto-generated function: test_utils_default_tz_info_naive"""
    try:
        response = dateutil.test_utils_default_tz_info_naive()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_default_tz_info_aware():
    """Auto-generated function: test_utils_default_tz_info_aware"""
    try:
        response = dateutil.test_utils_default_tz_info_aware()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_within_delta():
    """Auto-generated function: test_utils_within_delta"""
    try:
        response = dateutil.test_utils_within_delta()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_utils_within_delta_with_negative_delta():
    """Auto-generated function: test_utils_within_delta_with_negative_delta"""
    try:
        response = dateutil.test_utils_within_delta_with_negative_delta()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def assertPicklable(obj, singleton, asfile, dump_kwargs, load_kwargs):
    """Auto-generated function: assertPicklable"""
    try:
        response = dateutil.PicklableMixin.assertPicklable(obj, singleton, asfile, dump_kwargs, load_kwargs)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tz_change_allowed(cls):
    """Auto-generated function: tz_change_allowed"""
    try:
        response = dateutil.TZContextBase.tz_change_allowed(cls)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def tz_change_disallowed_message(cls):
    """Auto-generated function: tz_change_disallowed_message"""
    try:
        response = dateutil.TZContextBase.tz_change_disallowed_message(cls)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_current_tz():
    """Auto-generated function: get_current_tz"""
    try:
        response = dateutil.TZWinContext.get_current_tz()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def set_current_tz(tzname):
    """Auto-generated function: set_current_tz"""
    try:
        response = dateutil.TZWinContext.set_current_tz(tzname)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def fuzzy(request):
    """Auto-generated function: fuzzy"""
    try:
        response = dateutil.fuzzy(request)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parser(parsable_text, expected_datetime, assertion_message):
    """Auto-generated function: test_parser"""
    try:
        response = dateutil.test_parser(parsable_text, expected_datetime, assertion_message)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parser_default(parsable_text, expected_datetime, assertion_message):
    """Auto-generated function: test_parser_default"""
    try:
        response = dateutil.test_parser_default(parsable_text, expected_datetime, assertion_message)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_dayfirst(sep):
    """Auto-generated function: test_parse_dayfirst"""
    try:
        response = dateutil.test_parse_dayfirst(sep)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_yearfirst(sep):
    """Auto-generated function: test_parse_yearfirst"""
    try:
        response = dateutil.test_parse_yearfirst(sep)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_ignoretz(dstr, expected):
    """Auto-generated function: test_parse_ignoretz"""
    try:
        response = dateutil.test_parse_ignoretz(dstr, expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_with_tzoffset(dstr, expected):
    """Auto-generated function: test_parse_with_tzoffset"""
    try:
        response = dateutil.test_parse_with_tzoffset(dstr, expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ybd():
    """Auto-generated function: test_ybd"""
    try:
        response = dateutil.TestFormat.test_ybd()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_strftime_formats_2003Sep25(fmt, dstr):
    """Auto-generated function: test_strftime_formats_2003Sep25"""
    try:
        response = dateutil.TestFormat.test_strftime_formats_2003Sep25(fmt, dstr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_empty_string_invalid():
    """Auto-generated function: test_empty_string_invalid"""
    try:
        response = dateutil.TestInputTypes.test_empty_string_invalid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_none_invalid():
    """Auto-generated function: test_none_invalid"""
    try:
        response = dateutil.TestInputTypes.test_none_invalid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_int_invalid():
    """Auto-generated function: test_int_invalid"""
    try:
        response = dateutil.TestInputTypes.test_int_invalid()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_duck_typing():
    """Auto-generated function: test_duck_typing"""
    try:
        response = dateutil.TestInputTypes.test_duck_typing()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_stream():
    """Auto-generated function: test_parse_stream"""
    try:
        response = dateutil.TestInputTypes.test_parse_stream()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_str():
    """Auto-generated function: test_parse_str"""
    try:
        response = dateutil.TestInputTypes.test_parse_str()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_bytes():
    """Auto-generated function: test_parse_bytes"""
    try:
        response = dateutil.TestInputTypes.test_parse_bytes()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_bytearray():
    """Auto-generated function: test_parse_bytearray"""
    try:
        response = dateutil.TestInputTypes.test_parse_bytearray()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def assert_equal_same_tz(dt1, dt2):
    """Auto-generated function: assert_equal_same_tz"""
    try:
        response = dateutil.TestTzinfoInputTypes.assert_equal_same_tz(dt1, dt2)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzinfo_dict_could_return_none():
    """Auto-generated function: test_tzinfo_dict_could_return_none"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_tzinfo_dict_could_return_none()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzinfos_callable_could_return_none():
    """Auto-generated function: test_tzinfos_callable_could_return_none"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_tzinfos_callable_could_return_none()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_invalid_tzinfo_input():
    """Auto-generated function: test_invalid_tzinfo_input"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_invalid_tzinfo_input()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_tzinfo_tzinfo_input():
    """Auto-generated function: test_valid_tzinfo_tzinfo_input"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_valid_tzinfo_tzinfo_input()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_tzinfo_unicode_input():
    """Auto-generated function: test_valid_tzinfo_unicode_input"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_valid_tzinfo_unicode_input()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_tzinfo_callable_input():
    """Auto-generated function: test_valid_tzinfo_callable_input"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_valid_tzinfo_callable_input()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_valid_tzinfo_int_input():
    """Auto-generated function: test_valid_tzinfo_int_input"""
    try:
        response = dateutil.TestTzinfoInputTypes.test_valid_tzinfo_int_input()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def setup_class(cls):
    """Auto-generated function: setup_class"""
    try:
        response = dateutil.ParserTest.setup_class(cls)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testParserParseStr():
    """Auto-generated function: testParserParseStr"""
    try:
        response = dateutil.ParserTest.testParserParseStr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testParseUnicodeWords():
    """Auto-generated function: testParseUnicodeWords"""
    try:
        response = dateutil.ParserTest.testParseUnicodeWords()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testParseWithNulls():
    """Auto-generated function: testParseWithNulls"""
    try:
        response = dateutil.ParserTest.testParseWithNulls()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDateCommandFormat():
    """Auto-generated function: testDateCommandFormat"""
    try:
        response = dateutil.ParserTest.testDateCommandFormat()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDateCommandFormatReversed():
    """Auto-generated function: testDateCommandFormatReversed"""
    try:
        response = dateutil.ParserTest.testDateCommandFormatReversed()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDateCommandFormatWithLong():
    """Auto-generated function: testDateCommandFormatWithLong"""
    try:
        response = dateutil.ParserTest.testDateCommandFormatWithLong()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testISOFormatStrip2():
    """Auto-generated function: testISOFormatStrip2"""
    try:
        response = dateutil.ParserTest.testISOFormatStrip2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testISOStrippedFormatStrip2():
    """Auto-generated function: testISOStrippedFormatStrip2"""
    try:
        response = dateutil.ParserTest.testISOStrippedFormatStrip2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAMPMNoHour():
    """Auto-generated function: testAMPMNoHour"""
    try:
        response = dateutil.ParserTest.testAMPMNoHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAMPMRange():
    """Auto-generated function: testAMPMRange"""
    try:
        response = dateutil.ParserTest.testAMPMRange()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testPertain():
    """Auto-generated function: testPertain"""
    try:
        response = dateutil.ParserTest.testPertain()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFuzzy():
    """Auto-generated function: testFuzzy"""
    try:
        response = dateutil.ParserTest.testFuzzy()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFuzzyWithTokens():
    """Auto-generated function: testFuzzyWithTokens"""
    try:
        response = dateutil.ParserTest.testFuzzyWithTokens()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFuzzyAMPMProblem():
    """Auto-generated function: testFuzzyAMPMProblem"""
    try:
        response = dateutil.ParserTest.testFuzzyAMPMProblem()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testFuzzyIgnoreAMPM():
    """Auto-generated function: testFuzzyIgnoreAMPM"""
    try:
        response = dateutil.ParserTest.testFuzzyIgnoreAMPM()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRandomFormat24():
    """Auto-generated function: testRandomFormat24"""
    try:
        response = dateutil.ParserTest.testRandomFormat24()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testRandomFormat26():
    """Auto-generated function: testRandomFormat26"""
    try:
        response = dateutil.ParserTest.testRandomFormat26()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnspecifiedDayFallback():
    """Auto-generated function: testUnspecifiedDayFallback"""
    try:
        response = dateutil.ParserTest.testUnspecifiedDayFallback()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnspecifiedDayFallbackFebNoLeapYear():
    """Auto-generated function: testUnspecifiedDayFallbackFebNoLeapYear"""
    try:
        response = dateutil.ParserTest.testUnspecifiedDayFallbackFebNoLeapYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnspecifiedDayFallbackFebLeapYear():
    """Auto-generated function: testUnspecifiedDayFallbackFebLeapYear"""
    try:
        response = dateutil.ParserTest.testUnspecifiedDayFallbackFebLeapYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testErrorType01():
    """Auto-generated function: testErrorType01"""
    try:
        response = dateutil.ParserTest.testErrorType01()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCorrectErrorOnFuzzyWithTokens():
    """Auto-generated function: testCorrectErrorOnFuzzyWithTokens"""
    try:
        response = dateutil.ParserTest.testCorrectErrorOnFuzzyWithTokens()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncreasingCTime():
    """Auto-generated function: testIncreasingCTime"""
    try:
        response = dateutil.ParserTest.testIncreasingCTime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testIncreasingISOFormat():
    """Auto-generated function: testIncreasingISOFormat"""
    try:
        response = dateutil.ParserTest.testIncreasingISOFormat()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMicrosecondsPrecisionError():
    """Auto-generated function: testMicrosecondsPrecisionError"""
    try:
        response = dateutil.ParserTest.testMicrosecondsPrecisionError()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMicrosecondPrecisionErrorReturns():
    """Auto-generated function: testMicrosecondPrecisionErrorReturns"""
    try:
        response = dateutil.ParserTest.testMicrosecondPrecisionErrorReturns()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCustomParserInfo():
    """Auto-generated function: testCustomParserInfo"""
    try:
        response = dateutil.ParserTest.testCustomParserInfo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCustomParserShortDaynames():
    """Auto-generated function: testCustomParserShortDaynames"""
    try:
        response = dateutil.ParserTest.testCustomParserShortDaynames()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testNoYearFirstNoDayFirst():
    """Auto-generated function: testNoYearFirstNoDayFirst"""
    try:
        response = dateutil.ParserTest.testNoYearFirstNoDayFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearFirst():
    """Auto-generated function: testYearFirst"""
    try:
        response = dateutil.ParserTest.testYearFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDayFirst():
    """Auto-generated function: testDayFirst"""
    try:
        response = dateutil.ParserTest.testDayFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDayFirstYearFirst():
    """Auto-generated function: testDayFirstYearFirst"""
    try:
        response = dateutil.ParserTest.testDayFirstYearFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousYearFirst():
    """Auto-generated function: testUnambiguousYearFirst"""
    try:
        response = dateutil.ParserTest.testUnambiguousYearFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousDayFirst():
    """Auto-generated function: testUnambiguousDayFirst"""
    try:
        response = dateutil.ParserTest.testUnambiguousDayFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUnambiguousDayFirstYearFirst():
    """Auto-generated function: testUnambiguousDayFirstYearFirst"""
    try:
        response = dateutil.ParserTest.testUnambiguousDayFirstYearFirst()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_mstridx():
    """Auto-generated function: test_mstridx"""
    try:
        response = dateutil.ParserTest.test_mstridx()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_idx_check():
    """Auto-generated function: test_idx_check"""
    try:
        response = dateutil.ParserTest.test_idx_check()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_hmBY():
    """Auto-generated function: test_hmBY"""
    try:
        response = dateutil.ParserTest.test_hmBY()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_validate_hour():
    """Auto-generated function: test_validate_hour"""
    try:
        response = dateutil.ParserTest.test_validate_hour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_era_trailing_year():
    """Auto-generated function: test_era_trailing_year"""
    try:
        response = dateutil.ParserTest.test_era_trailing_year()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_includes_timestr():
    """Auto-generated function: test_includes_timestr"""
    try:
        response = dateutil.ParserTest.test_includes_timestr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_no_year_zero():
    """Auto-generated function: test_no_year_zero"""
    try:
        response = dateutil.TestOutOfBounds.test_no_year_zero()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_out_of_bound_day():
    """Auto-generated function: test_out_of_bound_day"""
    try:
        response = dateutil.TestOutOfBounds.test_out_of_bound_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_illegal_month_error():
    """Auto-generated function: test_illegal_month_error"""
    try:
        response = dateutil.TestOutOfBounds.test_illegal_month_error()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_day_sanity(fuzzy):
    """Auto-generated function: test_day_sanity"""
    try:
        response = dateutil.TestOutOfBounds.test_day_sanity(fuzzy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_minute_sanity(fuzzy):
    """Auto-generated function: test_minute_sanity"""
    try:
        response = dateutil.TestOutOfBounds.test_minute_sanity(fuzzy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_hour_sanity(fuzzy):
    """Auto-generated function: test_hour_sanity"""
    try:
        response = dateutil.TestOutOfBounds.test_hour_sanity(fuzzy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_second_sanity(fuzzy):
    """Auto-generated function: test_second_sanity"""
    try:
        response = dateutil.TestOutOfBounds.test_second_sanity(fuzzy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_somewhat_ambiguous_string():
    """Auto-generated function: test_somewhat_ambiguous_string"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_somewhat_ambiguous_string()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_YmdH_M_S():
    """Auto-generated function: test_YmdH_M_S"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_YmdH_M_S()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_first_century():
    """Auto-generated function: test_first_century"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_first_century()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_era_trailing_year_with_dots():
    """Auto-generated function: test_era_trailing_year_with_dots"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_era_trailing_year_with_dots()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ad_nospace():
    """Auto-generated function: test_ad_nospace"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_ad_nospace()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_four_letter_day():
    """Auto-generated function: test_four_letter_day"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_four_letter_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_non_date_number():
    """Auto-generated function: test_non_date_number"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_non_date_number()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_on_era():
    """Auto-generated function: test_on_era"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_on_era()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extraneous_year():
    """Auto-generated function: test_extraneous_year"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_extraneous_year()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extraneous_year_tokens():
    """Auto-generated function: test_extraneous_year_tokens"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_extraneous_year_tokens()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extraneous_year2():
    """Auto-generated function: test_extraneous_year2"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_extraneous_year2()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extraneous_year3():
    """Auto-generated function: test_extraneous_year3"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_extraneous_year3()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_unambiguous_YYYYMM():
    """Auto-generated function: test_unambiguous_YYYYMM"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_unambiguous_YYYYMM()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extraneous_numerical_content():
    """Auto-generated function: test_extraneous_numerical_content"""
    try:
        response = dateutil.TestParseUnimplementedCases.test_extraneous_numerical_content()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_unambiguous_nonexistent_local():
    """Auto-generated function: test_parse_unambiguous_nonexistent_local"""
    try:
        response = dateutil.TestTZVar.test_parse_unambiguous_nonexistent_local()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_in_gmt():
    """Auto-generated function: test_tzlocal_in_gmt"""
    try:
        response = dateutil.TestTZVar.test_tzlocal_in_gmt()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzlocal_parse_fold():
    """Auto-generated function: test_tzlocal_parse_fold"""
    try:
        response = dateutil.TestTZVar.test_tzlocal_parse_fold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_tzinfos_fold():
    """Auto-generated function: test_parse_tzinfos_fold"""
    try:
        response = dateutil.test_parse_tzinfos_fold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_rounding_floatlike_strings(dtstr, dt):
    """Auto-generated function: test_rounding_floatlike_strings"""
    try:
        response = dateutil.test_rounding_floatlike_strings(dtstr, dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_decimal_error(value):
    """Auto-generated function: test_decimal_error"""
    try:
        response = dateutil.test_decimal_error(value)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parsererror_repr():
    """Auto-generated function: test_parsererror_repr"""
    try:
        response = dateutil.test_parsererror_repr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrAppendRRULEToken():
    """Auto-generated function: testStrAppendRRULEToken"""
    try:
        response = dateutil.RRuleTest.testStrAppendRRULEToken()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearly():
    """Auto-generated function: testYearly"""
    try:
        response = dateutil.RRuleTest.testYearly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyInterval():
    """Auto-generated function: testYearlyInterval"""
    try:
        response = dateutil.RRuleTest.testYearlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyIntervalLarge():
    """Auto-generated function: testYearlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testYearlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonth():
    """Auto-generated function: testYearlyByMonth"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthDay():
    """Auto-generated function: testYearlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndMonthDay():
    """Auto-generated function: testYearlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekDay():
    """Auto-generated function: testYearlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByNWeekDay():
    """Auto-generated function: testYearlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByNWeekDayLarge():
    """Auto-generated function: testYearlyByNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testYearlyByNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndWeekDay():
    """Auto-generated function: testYearlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndNWeekDay():
    """Auto-generated function: testYearlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndNWeekDayLarge():
    """Auto-generated function: testYearlyByMonthAndNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthDayAndWeekDay():
    """Auto-generated function: testYearlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testYearlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByYearDay():
    """Auto-generated function: testYearlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByYearDayNeg():
    """Auto-generated function: testYearlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testYearlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndYearDay():
    """Auto-generated function: testYearlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMonthAndYearDayNeg():
    """Auto-generated function: testYearlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testYearlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekNo():
    """Auto-generated function: testYearlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekNoAndWeekDay():
    """Auto-generated function: testYearlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testYearlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testYearlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByEaster():
    """Auto-generated function: testYearlyByEaster"""
    try:
        response = dateutil.RRuleTest.testYearlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByEasterPos():
    """Auto-generated function: testYearlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testYearlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByEasterNeg():
    """Auto-generated function: testYearlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testYearlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByWeekNoAndWeekDay53():
    """Auto-generated function: testYearlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testYearlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByHour():
    """Auto-generated function: testYearlyByHour"""
    try:
        response = dateutil.RRuleTest.testYearlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMinute():
    """Auto-generated function: testYearlyByMinute"""
    try:
        response = dateutil.RRuleTest.testYearlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyBySecond():
    """Auto-generated function: testYearlyBySecond"""
    try:
        response = dateutil.RRuleTest.testYearlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByHourAndMinute():
    """Auto-generated function: testYearlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testYearlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByHourAndSecond():
    """Auto-generated function: testYearlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testYearlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByMinuteAndSecond():
    """Auto-generated function: testYearlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testYearlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyByHourAndMinuteAndSecond():
    """Auto-generated function: testYearlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testYearlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testYearlyBySetPos():
    """Auto-generated function: testYearlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testYearlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthly():
    """Auto-generated function: testMonthly"""
    try:
        response = dateutil.RRuleTest.testMonthly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyInterval():
    """Auto-generated function: testMonthlyInterval"""
    try:
        response = dateutil.RRuleTest.testMonthlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyIntervalLarge():
    """Auto-generated function: testMonthlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testMonthlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonth():
    """Auto-generated function: testMonthlyByMonth"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthDay():
    """Auto-generated function: testMonthlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndMonthDay():
    """Auto-generated function: testMonthlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekDay():
    """Auto-generated function: testMonthlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByNWeekDay():
    """Auto-generated function: testMonthlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByNWeekDayLarge():
    """Auto-generated function: testMonthlyByNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testMonthlyByNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndWeekDay():
    """Auto-generated function: testMonthlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndNWeekDay():
    """Auto-generated function: testMonthlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndNWeekDayLarge():
    """Auto-generated function: testMonthlyByMonthAndNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthDayAndWeekDay():
    """Auto-generated function: testMonthlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testMonthlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByYearDay():
    """Auto-generated function: testMonthlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByYearDayNeg():
    """Auto-generated function: testMonthlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testMonthlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndYearDay():
    """Auto-generated function: testMonthlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMonthAndYearDayNeg():
    """Auto-generated function: testMonthlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekNo():
    """Auto-generated function: testMonthlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekNoAndWeekDay():
    """Auto-generated function: testMonthlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testMonthlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testMonthlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByWeekNoAndWeekDay53():
    """Auto-generated function: testMonthlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testMonthlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByEaster():
    """Auto-generated function: testMonthlyByEaster"""
    try:
        response = dateutil.RRuleTest.testMonthlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByEasterPos():
    """Auto-generated function: testMonthlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testMonthlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByEasterNeg():
    """Auto-generated function: testMonthlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testMonthlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByHour():
    """Auto-generated function: testMonthlyByHour"""
    try:
        response = dateutil.RRuleTest.testMonthlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMinute():
    """Auto-generated function: testMonthlyByMinute"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyBySecond():
    """Auto-generated function: testMonthlyBySecond"""
    try:
        response = dateutil.RRuleTest.testMonthlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByHourAndMinute():
    """Auto-generated function: testMonthlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testMonthlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByHourAndSecond():
    """Auto-generated function: testMonthlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testMonthlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByMinuteAndSecond():
    """Auto-generated function: testMonthlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testMonthlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyByHourAndMinuteAndSecond():
    """Auto-generated function: testMonthlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testMonthlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMonthlyBySetPos():
    """Auto-generated function: testMonthlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testMonthlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekly():
    """Auto-generated function: testWeekly"""
    try:
        response = dateutil.RRuleTest.testWeekly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyInterval():
    """Auto-generated function: testWeeklyInterval"""
    try:
        response = dateutil.RRuleTest.testWeeklyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyIntervalLarge():
    """Auto-generated function: testWeeklyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testWeeklyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonth():
    """Auto-generated function: testWeeklyByMonth"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthDay():
    """Auto-generated function: testWeeklyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndMonthDay():
    """Auto-generated function: testWeeklyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekDay():
    """Auto-generated function: testWeeklyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByNWeekDay():
    """Auto-generated function: testWeeklyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndWeekDay():
    """Auto-generated function: testWeeklyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndNWeekDay():
    """Auto-generated function: testWeeklyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthDayAndWeekDay():
    """Auto-generated function: testWeeklyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testWeeklyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByYearDay():
    """Auto-generated function: testWeeklyByYearDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByYearDayNeg():
    """Auto-generated function: testWeeklyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testWeeklyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndYearDay():
    """Auto-generated function: testWeeklyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMonthAndYearDayNeg():
    """Auto-generated function: testWeeklyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekNo():
    """Auto-generated function: testWeeklyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekNoAndWeekDay():
    """Auto-generated function: testWeeklyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testWeeklyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekNoAndWeekDayLast():
    """Auto-generated function: testWeeklyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByWeekNoAndWeekDay53():
    """Auto-generated function: testWeeklyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testWeeklyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByEaster():
    """Auto-generated function: testWeeklyByEaster"""
    try:
        response = dateutil.RRuleTest.testWeeklyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByEasterPos():
    """Auto-generated function: testWeeklyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testWeeklyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByEasterNeg():
    """Auto-generated function: testWeeklyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testWeeklyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByHour():
    """Auto-generated function: testWeeklyByHour"""
    try:
        response = dateutil.RRuleTest.testWeeklyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMinute():
    """Auto-generated function: testWeeklyByMinute"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyBySecond():
    """Auto-generated function: testWeeklyBySecond"""
    try:
        response = dateutil.RRuleTest.testWeeklyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByHourAndMinute():
    """Auto-generated function: testWeeklyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testWeeklyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByHourAndSecond():
    """Auto-generated function: testWeeklyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testWeeklyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByMinuteAndSecond():
    """Auto-generated function: testWeeklyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testWeeklyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyByHourAndMinuteAndSecond():
    """Auto-generated function: testWeeklyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testWeeklyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeeklyBySetPos():
    """Auto-generated function: testWeeklyBySetPos"""
    try:
        response = dateutil.RRuleTest.testWeeklyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDaily():
    """Auto-generated function: testDaily"""
    try:
        response = dateutil.RRuleTest.testDaily()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyInterval():
    """Auto-generated function: testDailyInterval"""
    try:
        response = dateutil.RRuleTest.testDailyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyIntervalLarge():
    """Auto-generated function: testDailyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testDailyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonth():
    """Auto-generated function: testDailyByMonth"""
    try:
        response = dateutil.RRuleTest.testDailyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthDay():
    """Auto-generated function: testDailyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndMonthDay():
    """Auto-generated function: testDailyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekDay():
    """Auto-generated function: testDailyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByNWeekDay():
    """Auto-generated function: testDailyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndWeekDay():
    """Auto-generated function: testDailyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndNWeekDay():
    """Auto-generated function: testDailyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthDayAndWeekDay():
    """Auto-generated function: testDailyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testDailyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByYearDay():
    """Auto-generated function: testDailyByYearDay"""
    try:
        response = dateutil.RRuleTest.testDailyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByYearDayNeg():
    """Auto-generated function: testDailyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testDailyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndYearDay():
    """Auto-generated function: testDailyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMonthAndYearDayNeg():
    """Auto-generated function: testDailyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testDailyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekNo():
    """Auto-generated function: testDailyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekNoAndWeekDay():
    """Auto-generated function: testDailyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testDailyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekNoAndWeekDayLast():
    """Auto-generated function: testDailyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByWeekNoAndWeekDay53():
    """Auto-generated function: testDailyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testDailyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByEaster():
    """Auto-generated function: testDailyByEaster"""
    try:
        response = dateutil.RRuleTest.testDailyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByEasterPos():
    """Auto-generated function: testDailyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testDailyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByEasterNeg():
    """Auto-generated function: testDailyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testDailyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByHour():
    """Auto-generated function: testDailyByHour"""
    try:
        response = dateutil.RRuleTest.testDailyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMinute():
    """Auto-generated function: testDailyByMinute"""
    try:
        response = dateutil.RRuleTest.testDailyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyBySecond():
    """Auto-generated function: testDailyBySecond"""
    try:
        response = dateutil.RRuleTest.testDailyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByHourAndMinute():
    """Auto-generated function: testDailyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testDailyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByHourAndSecond():
    """Auto-generated function: testDailyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testDailyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByMinuteAndSecond():
    """Auto-generated function: testDailyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testDailyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyByHourAndMinuteAndSecond():
    """Auto-generated function: testDailyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testDailyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDailyBySetPos():
    """Auto-generated function: testDailyBySetPos"""
    try:
        response = dateutil.RRuleTest.testDailyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourly():
    """Auto-generated function: testHourly"""
    try:
        response = dateutil.RRuleTest.testHourly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyInterval():
    """Auto-generated function: testHourlyInterval"""
    try:
        response = dateutil.RRuleTest.testHourlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyIntervalLarge():
    """Auto-generated function: testHourlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testHourlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonth():
    """Auto-generated function: testHourlyByMonth"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthDay():
    """Auto-generated function: testHourlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndMonthDay():
    """Auto-generated function: testHourlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekDay():
    """Auto-generated function: testHourlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByNWeekDay():
    """Auto-generated function: testHourlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndWeekDay():
    """Auto-generated function: testHourlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndNWeekDay():
    """Auto-generated function: testHourlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthDayAndWeekDay():
    """Auto-generated function: testHourlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testHourlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByYearDay():
    """Auto-generated function: testHourlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByYearDayNeg():
    """Auto-generated function: testHourlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testHourlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndYearDay():
    """Auto-generated function: testHourlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMonthAndYearDayNeg():
    """Auto-generated function: testHourlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testHourlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekNo():
    """Auto-generated function: testHourlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekNoAndWeekDay():
    """Auto-generated function: testHourlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testHourlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testHourlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByWeekNoAndWeekDay53():
    """Auto-generated function: testHourlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testHourlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByEaster():
    """Auto-generated function: testHourlyByEaster"""
    try:
        response = dateutil.RRuleTest.testHourlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByEasterPos():
    """Auto-generated function: testHourlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testHourlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByEasterNeg():
    """Auto-generated function: testHourlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testHourlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByHour():
    """Auto-generated function: testHourlyByHour"""
    try:
        response = dateutil.RRuleTest.testHourlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMinute():
    """Auto-generated function: testHourlyByMinute"""
    try:
        response = dateutil.RRuleTest.testHourlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyBySecond():
    """Auto-generated function: testHourlyBySecond"""
    try:
        response = dateutil.RRuleTest.testHourlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByHourAndMinute():
    """Auto-generated function: testHourlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testHourlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByHourAndSecond():
    """Auto-generated function: testHourlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testHourlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByMinuteAndSecond():
    """Auto-generated function: testHourlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testHourlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyByHourAndMinuteAndSecond():
    """Auto-generated function: testHourlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testHourlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyBySetPos():
    """Auto-generated function: testHourlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testHourlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutely():
    """Auto-generated function: testMinutely"""
    try:
        response = dateutil.RRuleTest.testMinutely()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyInterval():
    """Auto-generated function: testMinutelyInterval"""
    try:
        response = dateutil.RRuleTest.testMinutelyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyIntervalLarge():
    """Auto-generated function: testMinutelyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testMinutelyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonth():
    """Auto-generated function: testMinutelyByMonth"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthDay():
    """Auto-generated function: testMinutelyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndMonthDay():
    """Auto-generated function: testMinutelyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekDay():
    """Auto-generated function: testMinutelyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByNWeekDay():
    """Auto-generated function: testMinutelyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndWeekDay():
    """Auto-generated function: testMinutelyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndNWeekDay():
    """Auto-generated function: testMinutelyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthDayAndWeekDay():
    """Auto-generated function: testMinutelyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testMinutelyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByYearDay():
    """Auto-generated function: testMinutelyByYearDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByYearDayNeg():
    """Auto-generated function: testMinutelyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testMinutelyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndYearDay():
    """Auto-generated function: testMinutelyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMonthAndYearDayNeg():
    """Auto-generated function: testMinutelyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekNo():
    """Auto-generated function: testMinutelyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekNoAndWeekDay():
    """Auto-generated function: testMinutelyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testMinutelyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekNoAndWeekDayLast():
    """Auto-generated function: testMinutelyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByWeekNoAndWeekDay53():
    """Auto-generated function: testMinutelyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testMinutelyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByEaster():
    """Auto-generated function: testMinutelyByEaster"""
    try:
        response = dateutil.RRuleTest.testMinutelyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByEasterPos():
    """Auto-generated function: testMinutelyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testMinutelyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByEasterNeg():
    """Auto-generated function: testMinutelyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testMinutelyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByHour():
    """Auto-generated function: testMinutelyByHour"""
    try:
        response = dateutil.RRuleTest.testMinutelyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMinute():
    """Auto-generated function: testMinutelyByMinute"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyBySecond():
    """Auto-generated function: testMinutelyBySecond"""
    try:
        response = dateutil.RRuleTest.testMinutelyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByHourAndMinute():
    """Auto-generated function: testMinutelyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testMinutelyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByHourAndSecond():
    """Auto-generated function: testMinutelyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testMinutelyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByMinuteAndSecond():
    """Auto-generated function: testMinutelyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testMinutelyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyByHourAndMinuteAndSecond():
    """Auto-generated function: testMinutelyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testMinutelyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyBySetPos():
    """Auto-generated function: testMinutelyBySetPos"""
    try:
        response = dateutil.RRuleTest.testMinutelyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondly():
    """Auto-generated function: testSecondly"""
    try:
        response = dateutil.RRuleTest.testSecondly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyInterval():
    """Auto-generated function: testSecondlyInterval"""
    try:
        response = dateutil.RRuleTest.testSecondlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyIntervalLarge():
    """Auto-generated function: testSecondlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testSecondlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonth():
    """Auto-generated function: testSecondlyByMonth"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthDay():
    """Auto-generated function: testSecondlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndMonthDay():
    """Auto-generated function: testSecondlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekDay():
    """Auto-generated function: testSecondlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByNWeekDay():
    """Auto-generated function: testSecondlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndWeekDay():
    """Auto-generated function: testSecondlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndNWeekDay():
    """Auto-generated function: testSecondlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthDayAndWeekDay():
    """Auto-generated function: testSecondlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testSecondlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByYearDay():
    """Auto-generated function: testSecondlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByYearDayNeg():
    """Auto-generated function: testSecondlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testSecondlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndYearDay():
    """Auto-generated function: testSecondlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMonthAndYearDayNeg():
    """Auto-generated function: testSecondlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekNo():
    """Auto-generated function: testSecondlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekNoAndWeekDay():
    """Auto-generated function: testSecondlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testSecondlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testSecondlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByWeekNoAndWeekDay53():
    """Auto-generated function: testSecondlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testSecondlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByEaster():
    """Auto-generated function: testSecondlyByEaster"""
    try:
        response = dateutil.RRuleTest.testSecondlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByEasterPos():
    """Auto-generated function: testSecondlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testSecondlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByEasterNeg():
    """Auto-generated function: testSecondlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testSecondlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByHour():
    """Auto-generated function: testSecondlyByHour"""
    try:
        response = dateutil.RRuleTest.testSecondlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMinute():
    """Auto-generated function: testSecondlyByMinute"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyBySecond():
    """Auto-generated function: testSecondlyBySecond"""
    try:
        response = dateutil.RRuleTest.testSecondlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByHourAndMinute():
    """Auto-generated function: testSecondlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testSecondlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByHourAndSecond():
    """Auto-generated function: testSecondlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testSecondlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByMinuteAndSecond():
    """Auto-generated function: testSecondlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testSecondlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByHourAndMinuteAndSecond():
    """Auto-generated function: testSecondlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testSecondlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyByHourAndMinuteAndSecondBug():
    """Auto-generated function: testSecondlyByHourAndMinuteAndSecondBug"""
    try:
        response = dateutil.RRuleTest.testSecondlyByHourAndMinuteAndSecondBug()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testLongIntegers():
    """Auto-generated function: testLongIntegers"""
    try:
        response = dateutil.RRuleTest.testLongIntegers()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testHourlyBadRRule():
    """Auto-generated function: testHourlyBadRRule"""
    try:
        response = dateutil.RRuleTest.testHourlyBadRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyBadRRule():
    """Auto-generated function: testMinutelyBadRRule"""
    try:
        response = dateutil.RRuleTest.testMinutelyBadRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyBadRRule():
    """Auto-generated function: testSecondlyBadRRule"""
    try:
        response = dateutil.RRuleTest.testSecondlyBadRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMinutelyBadComboRRule():
    """Auto-generated function: testMinutelyBadComboRRule"""
    try:
        response = dateutil.RRuleTest.testMinutelyBadComboRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSecondlyBadComboRRule():
    """Auto-generated function: testSecondlyBadComboRRule"""
    try:
        response = dateutil.RRuleTest.testSecondlyBadComboRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBadUntilCountRRule():
    """Auto-generated function: testBadUntilCountRRule"""
    try:
        response = dateutil.RRuleTest.testBadUntilCountRRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUntilNotMatching():
    """Auto-generated function: testUntilNotMatching"""
    try:
        response = dateutil.RRuleTest.testUntilNotMatching()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUntilMatching():
    """Auto-generated function: testUntilMatching"""
    try:
        response = dateutil.RRuleTest.testUntilMatching()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUntilSingle():
    """Auto-generated function: testUntilSingle"""
    try:
        response = dateutil.RRuleTest.testUntilSingle()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUntilEmpty():
    """Auto-generated function: testUntilEmpty"""
    try:
        response = dateutil.RRuleTest.testUntilEmpty()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testUntilWithDate():
    """Auto-generated function: testUntilWithDate"""
    try:
        response = dateutil.RRuleTest.testUntilWithDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWkStIntervalMO():
    """Auto-generated function: testWkStIntervalMO"""
    try:
        response = dateutil.RRuleTest.testWkStIntervalMO()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWkStIntervalSU():
    """Auto-generated function: testWkStIntervalSU"""
    try:
        response = dateutil.RRuleTest.testWkStIntervalSU()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDTStartIsDate():
    """Auto-generated function: testDTStartIsDate"""
    try:
        response = dateutil.RRuleTest.testDTStartIsDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testDTStartWithMicroseconds():
    """Auto-generated function: testDTStartWithMicroseconds"""
    try:
        response = dateutil.RRuleTest.testDTStartWithMicroseconds()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testMaxYear():
    """Auto-generated function: testMaxYear"""
    try:
        response = dateutil.RRuleTest.testMaxYear()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetItem():
    """Auto-generated function: testGetItem"""
    try:
        response = dateutil.RRuleTest.testGetItem()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetItemNeg():
    """Auto-generated function: testGetItemNeg"""
    try:
        response = dateutil.RRuleTest.testGetItemNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetItemSlice():
    """Auto-generated function: testGetItemSlice"""
    try:
        response = dateutil.RRuleTest.testGetItemSlice()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetItemSliceEmpty():
    """Auto-generated function: testGetItemSliceEmpty"""
    try:
        response = dateutil.RRuleTest.testGetItemSliceEmpty()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testGetItemSliceStep():
    """Auto-generated function: testGetItemSliceStep"""
    try:
        response = dateutil.RRuleTest.testGetItemSliceStep()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCount():
    """Auto-generated function: testCount"""
    try:
        response = dateutil.RRuleTest.testCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCountZero():
    """Auto-generated function: testCountZero"""
    try:
        response = dateutil.RRuleTest.testCountZero()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testContains():
    """Auto-generated function: testContains"""
    try:
        response = dateutil.RRuleTest.testContains()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testContainsNot():
    """Auto-generated function: testContainsNot"""
    try:
        response = dateutil.RRuleTest.testContainsNot()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBefore():
    """Auto-generated function: testBefore"""
    try:
        response = dateutil.RRuleTest.testBefore()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBeforeInc():
    """Auto-generated function: testBeforeInc"""
    try:
        response = dateutil.RRuleTest.testBeforeInc()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAfter():
    """Auto-generated function: testAfter"""
    try:
        response = dateutil.RRuleTest.testAfter()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testAfterInc():
    """Auto-generated function: testAfterInc"""
    try:
        response = dateutil.RRuleTest.testAfterInc()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testXAfter():
    """Auto-generated function: testXAfter"""
    try:
        response = dateutil.RRuleTest.testXAfter()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testXAfterInc():
    """Auto-generated function: testXAfterInc"""
    try:
        response = dateutil.RRuleTest.testXAfterInc()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBetween():
    """Auto-generated function: testBetween"""
    try:
        response = dateutil.RRuleTest.testBetween()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBetweenInc():
    """Auto-generated function: testBetweenInc"""
    try:
        response = dateutil.RRuleTest.testBetweenInc()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCachePre():
    """Auto-generated function: testCachePre"""
    try:
        response = dateutil.RRuleTest.testCachePre()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCachePost():
    """Auto-generated function: testCachePost"""
    try:
        response = dateutil.RRuleTest.testCachePost()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCachePostInternal():
    """Auto-generated function: testCachePostInternal"""
    try:
        response = dateutil.RRuleTest.testCachePostInternal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCachePreContains():
    """Auto-generated function: testCachePreContains"""
    try:
        response = dateutil.RRuleTest.testCachePreContains()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testCachePostContains():
    """Auto-generated function: testCachePostContains"""
    try:
        response = dateutil.RRuleTest.testCachePostContains()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStr():
    """Auto-generated function: testStr"""
    try:
        response = dateutil.RRuleTest.testStr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrWithTZID():
    """Auto-generated function: testStrWithTZID"""
    try:
        response = dateutil.RRuleTest.testStrWithTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrWithTZIDMapping():
    """Auto-generated function: testStrWithTZIDMapping"""
    try:
        response = dateutil.RRuleTest.testStrWithTZIDMapping()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrWithTZIDCallable():
    """Auto-generated function: testStrWithTZIDCallable"""
    try:
        response = dateutil.RRuleTest.testStrWithTZIDCallable()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrWithTZIDCallableFailure():
    """Auto-generated function: testStrWithTZIDCallableFailure"""
    try:
        response = dateutil.RRuleTest.testStrWithTZIDCallableFailure()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrWithConflictingTZID():
    """Auto-generated function: testStrWithConflictingTZID"""
    try:
        response = dateutil.RRuleTest.testStrWithConflictingTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrType():
    """Auto-generated function: testStrType"""
    try:
        response = dateutil.RRuleTest.testStrType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrForceSetType():
    """Auto-generated function: testStrForceSetType"""
    try:
        response = dateutil.RRuleTest.testStrForceSetType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetType():
    """Auto-generated function: testStrSetType"""
    try:
        response = dateutil.RRuleTest.testStrSetType()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrCase():
    """Auto-generated function: testStrCase"""
    try:
        response = dateutil.RRuleTest.testStrCase()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSpaces():
    """Auto-generated function: testStrSpaces"""
    try:
        response = dateutil.RRuleTest.testStrSpaces()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSpacesAndLines():
    """Auto-generated function: testStrSpacesAndLines"""
    try:
        response = dateutil.RRuleTest.testStrSpacesAndLines()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrNoDTStart():
    """Auto-generated function: testStrNoDTStart"""
    try:
        response = dateutil.RRuleTest.testStrNoDTStart()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrValueOnly():
    """Auto-generated function: testStrValueOnly"""
    try:
        response = dateutil.RRuleTest.testStrValueOnly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrUnfold():
    """Auto-generated function: testStrUnfold"""
    try:
        response = dateutil.RRuleTest.testStrUnfold()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSet():
    """Auto-generated function: testStrSet"""
    try:
        response = dateutil.RRuleTest.testStrSet()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetDate():
    """Auto-generated function: testStrSetDate"""
    try:
        response = dateutil.RRuleTest.testStrSetDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExRule():
    """Auto-generated function: testStrSetExRule"""
    try:
        response = dateutil.RRuleTest.testStrSetExRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDate():
    """Auto-generated function: testStrSetExDate"""
    try:
        response = dateutil.RRuleTest.testStrSetExDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateMultiple():
    """Auto-generated function: testStrSetExDateMultiple"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateMultiple()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateWithTZID():
    """Auto-generated function: testStrSetExDateWithTZID"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateWithTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateValueDateTimeNoTZID():
    """Auto-generated function: testStrSetExDateValueDateTimeNoTZID"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateValueDateTimeNoTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateValueMixDateTimeNoTZID():
    """Auto-generated function: testStrSetExDateValueMixDateTimeNoTZID"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateValueMixDateTimeNoTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateValueDateTimeWithTZID():
    """Auto-generated function: testStrSetExDateValueDateTimeWithTZID"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateValueDateTimeWithTZID()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetExDateValueDate():
    """Auto-generated function: testStrSetExDateValueDate"""
    try:
        response = dateutil.RRuleTest.testStrSetExDateValueDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetDateAndExDate():
    """Auto-generated function: testStrSetDateAndExDate"""
    try:
        response = dateutil.RRuleTest.testStrSetDateAndExDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrSetDateAndExRule():
    """Auto-generated function: testStrSetDateAndExRule"""
    try:
        response = dateutil.RRuleTest.testStrSetDateAndExRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrKeywords():
    """Auto-generated function: testStrKeywords"""
    try:
        response = dateutil.RRuleTest.testStrKeywords()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrNWeekDay():
    """Auto-generated function: testStrNWeekDay"""
    try:
        response = dateutil.RRuleTest.testStrNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrUntil():
    """Auto-generated function: testStrUntil"""
    try:
        response = dateutil.RRuleTest.testStrUntil()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrValueDatetime():
    """Auto-generated function: testStrValueDatetime"""
    try:
        response = dateutil.RRuleTest.testStrValueDatetime()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrValueDate():
    """Auto-generated function: testStrValueDate"""
    try:
        response = dateutil.RRuleTest.testStrValueDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrMultipleDTStartComma():
    """Auto-generated function: testStrMultipleDTStartComma"""
    try:
        response = dateutil.RRuleTest.testStrMultipleDTStartComma()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrInvalidUntil():
    """Auto-generated function: testStrInvalidUntil"""
    try:
        response = dateutil.RRuleTest.testStrInvalidUntil()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrUntilMustBeUTC():
    """Auto-generated function: testStrUntilMustBeUTC"""
    try:
        response = dateutil.RRuleTest.testStrUntilMustBeUTC()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrUntilWithTZ():
    """Auto-generated function: testStrUntilWithTZ"""
    try:
        response = dateutil.RRuleTest.testStrUntilWithTZ()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrEmptyByDay():
    """Auto-generated function: testStrEmptyByDay"""
    try:
        response = dateutil.RRuleTest.testStrEmptyByDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testStrInvalidByDay():
    """Auto-generated function: testStrInvalidByDay"""
    try:
        response = dateutil.RRuleTest.testStrInvalidByDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBadBySetPos():
    """Auto-generated function: testBadBySetPos"""
    try:
        response = dateutil.RRuleTest.testBadBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testBadBySetPosMany():
    """Auto-generated function: testBadBySetPosMany"""
    try:
        response = dateutil.RRuleTest.testBadBySetPosMany()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearly():
    """Auto-generated function: testToStrYearly"""
    try:
        response = dateutil.RRuleTest.testToStrYearly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyInterval():
    """Auto-generated function: testToStrYearlyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonth():
    """Auto-generated function: testToStrYearlyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthDay():
    """Auto-generated function: testToStrYearlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndMonthDay():
    """Auto-generated function: testToStrYearlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekDay():
    """Auto-generated function: testToStrYearlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByNWeekDay():
    """Auto-generated function: testToStrYearlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByNWeekDayLarge():
    """Auto-generated function: testToStrYearlyByNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndWeekDay():
    """Auto-generated function: testToStrYearlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndNWeekDay():
    """Auto-generated function: testToStrYearlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndNWeekDayLarge():
    """Auto-generated function: testToStrYearlyByMonthAndNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrYearlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrYearlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByYearDay():
    """Auto-generated function: testToStrYearlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByYearDayNeg():
    """Auto-generated function: testToStrYearlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndYearDay():
    """Auto-generated function: testToStrYearlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrYearlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekNo():
    """Auto-generated function: testToStrYearlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrYearlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrYearlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrYearlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByEaster():
    """Auto-generated function: testToStrYearlyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByEasterPos():
    """Auto-generated function: testToStrYearlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByEasterNeg():
    """Auto-generated function: testToStrYearlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrYearlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByHour():
    """Auto-generated function: testToStrYearlyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMinute():
    """Auto-generated function: testToStrYearlyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyBySecond():
    """Auto-generated function: testToStrYearlyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByHourAndMinute():
    """Auto-generated function: testToStrYearlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByHourAndSecond():
    """Auto-generated function: testToStrYearlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByMinuteAndSecond():
    """Auto-generated function: testToStrYearlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrYearlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrYearlyBySetPos():
    """Auto-generated function: testToStrYearlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrYearlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthly():
    """Auto-generated function: testToStrMonthly"""
    try:
        response = dateutil.RRuleTest.testToStrMonthly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyInterval():
    """Auto-generated function: testToStrMonthlyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyIntervalLarge():
    """Auto-generated function: testToStrMonthlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonth():
    """Auto-generated function: testToStrMonthlyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthDay():
    """Auto-generated function: testToStrMonthlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndMonthDay():
    """Auto-generated function: testToStrMonthlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekDay():
    """Auto-generated function: testToStrMonthlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByNWeekDay():
    """Auto-generated function: testToStrMonthlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByNWeekDayLarge():
    """Auto-generated function: testToStrMonthlyByNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndWeekDay():
    """Auto-generated function: testToStrMonthlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndNWeekDay():
    """Auto-generated function: testToStrMonthlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndNWeekDayLarge():
    """Auto-generated function: testToStrMonthlyByMonthAndNWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndNWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrMonthlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrMonthlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByYearDay():
    """Auto-generated function: testToStrMonthlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByYearDayNeg():
    """Auto-generated function: testToStrMonthlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndYearDay():
    """Auto-generated function: testToStrMonthlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrMonthlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekNo():
    """Auto-generated function: testToStrMonthlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrMonthlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrMonthlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrMonthlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrMonthlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByEaster():
    """Auto-generated function: testToStrMonthlyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByEasterPos():
    """Auto-generated function: testToStrMonthlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByEasterNeg():
    """Auto-generated function: testToStrMonthlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByHour():
    """Auto-generated function: testToStrMonthlyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMinute():
    """Auto-generated function: testToStrMonthlyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyBySecond():
    """Auto-generated function: testToStrMonthlyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByHourAndMinute():
    """Auto-generated function: testToStrMonthlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByHourAndSecond():
    """Auto-generated function: testToStrMonthlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByMinuteAndSecond():
    """Auto-generated function: testToStrMonthlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrMonthlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMonthlyBySetPos():
    """Auto-generated function: testToStrMonthlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrMonthlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeekly():
    """Auto-generated function: testToStrWeekly"""
    try:
        response = dateutil.RRuleTest.testToStrWeekly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyInterval():
    """Auto-generated function: testToStrWeeklyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyIntervalLarge():
    """Auto-generated function: testToStrWeeklyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonth():
    """Auto-generated function: testToStrWeeklyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthDay():
    """Auto-generated function: testToStrWeeklyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndMonthDay():
    """Auto-generated function: testToStrWeeklyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekDay():
    """Auto-generated function: testToStrWeeklyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByNWeekDay():
    """Auto-generated function: testToStrWeeklyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndWeekDay():
    """Auto-generated function: testToStrWeeklyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndNWeekDay():
    """Auto-generated function: testToStrWeeklyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrWeeklyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrWeeklyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByYearDay():
    """Auto-generated function: testToStrWeeklyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByYearDayNeg():
    """Auto-generated function: testToStrWeeklyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndYearDay():
    """Auto-generated function: testToStrWeeklyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrWeeklyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekNo():
    """Auto-generated function: testToStrWeeklyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrWeeklyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrWeeklyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrWeeklyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrWeeklyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByEaster():
    """Auto-generated function: testToStrWeeklyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByEasterPos():
    """Auto-generated function: testToStrWeeklyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByEasterNeg():
    """Auto-generated function: testToStrWeeklyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByHour():
    """Auto-generated function: testToStrWeeklyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMinute():
    """Auto-generated function: testToStrWeeklyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyBySecond():
    """Auto-generated function: testToStrWeeklyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByHourAndMinute():
    """Auto-generated function: testToStrWeeklyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByHourAndSecond():
    """Auto-generated function: testToStrWeeklyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByMinuteAndSecond():
    """Auto-generated function: testToStrWeeklyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrWeeklyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWeeklyBySetPos():
    """Auto-generated function: testToStrWeeklyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrWeeklyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDaily():
    """Auto-generated function: testToStrDaily"""
    try:
        response = dateutil.RRuleTest.testToStrDaily()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyInterval():
    """Auto-generated function: testToStrDailyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrDailyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyIntervalLarge():
    """Auto-generated function: testToStrDailyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrDailyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonth():
    """Auto-generated function: testToStrDailyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthDay():
    """Auto-generated function: testToStrDailyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndMonthDay():
    """Auto-generated function: testToStrDailyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekDay():
    """Auto-generated function: testToStrDailyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByNWeekDay():
    """Auto-generated function: testToStrDailyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndWeekDay():
    """Auto-generated function: testToStrDailyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndNWeekDay():
    """Auto-generated function: testToStrDailyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrDailyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrDailyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByYearDay():
    """Auto-generated function: testToStrDailyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByYearDayNeg():
    """Auto-generated function: testToStrDailyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndYearDay():
    """Auto-generated function: testToStrDailyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrDailyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekNo():
    """Auto-generated function: testToStrDailyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrDailyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrDailyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrDailyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrDailyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByEaster():
    """Auto-generated function: testToStrDailyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByEasterPos():
    """Auto-generated function: testToStrDailyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByEasterNeg():
    """Auto-generated function: testToStrDailyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByHour():
    """Auto-generated function: testToStrDailyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMinute():
    """Auto-generated function: testToStrDailyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyBySecond():
    """Auto-generated function: testToStrDailyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrDailyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByHourAndMinute():
    """Auto-generated function: testToStrDailyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByHourAndSecond():
    """Auto-generated function: testToStrDailyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByMinuteAndSecond():
    """Auto-generated function: testToStrDailyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrDailyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrDailyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrDailyBySetPos():
    """Auto-generated function: testToStrDailyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrDailyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourly():
    """Auto-generated function: testToStrHourly"""
    try:
        response = dateutil.RRuleTest.testToStrHourly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyInterval():
    """Auto-generated function: testToStrHourlyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyIntervalLarge():
    """Auto-generated function: testToStrHourlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonth():
    """Auto-generated function: testToStrHourlyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthDay():
    """Auto-generated function: testToStrHourlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndMonthDay():
    """Auto-generated function: testToStrHourlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekDay():
    """Auto-generated function: testToStrHourlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByNWeekDay():
    """Auto-generated function: testToStrHourlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndWeekDay():
    """Auto-generated function: testToStrHourlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndNWeekDay():
    """Auto-generated function: testToStrHourlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrHourlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrHourlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByYearDay():
    """Auto-generated function: testToStrHourlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByYearDayNeg():
    """Auto-generated function: testToStrHourlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndYearDay():
    """Auto-generated function: testToStrHourlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrHourlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekNo():
    """Auto-generated function: testToStrHourlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrHourlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrHourlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrHourlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrHourlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByEaster():
    """Auto-generated function: testToStrHourlyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByEasterPos():
    """Auto-generated function: testToStrHourlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByEasterNeg():
    """Auto-generated function: testToStrHourlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByHour():
    """Auto-generated function: testToStrHourlyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMinute():
    """Auto-generated function: testToStrHourlyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyBySecond():
    """Auto-generated function: testToStrHourlyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByHourAndMinute():
    """Auto-generated function: testToStrHourlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByHourAndSecond():
    """Auto-generated function: testToStrHourlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByMinuteAndSecond():
    """Auto-generated function: testToStrHourlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrHourlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrHourlyBySetPos():
    """Auto-generated function: testToStrHourlyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrHourlyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutely():
    """Auto-generated function: testToStrMinutely"""
    try:
        response = dateutil.RRuleTest.testToStrMinutely()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyInterval():
    """Auto-generated function: testToStrMinutelyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyIntervalLarge():
    """Auto-generated function: testToStrMinutelyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonth():
    """Auto-generated function: testToStrMinutelyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthDay():
    """Auto-generated function: testToStrMinutelyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndMonthDay():
    """Auto-generated function: testToStrMinutelyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekDay():
    """Auto-generated function: testToStrMinutelyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByNWeekDay():
    """Auto-generated function: testToStrMinutelyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndWeekDay():
    """Auto-generated function: testToStrMinutelyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndNWeekDay():
    """Auto-generated function: testToStrMinutelyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrMinutelyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrMinutelyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByYearDay():
    """Auto-generated function: testToStrMinutelyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByYearDayNeg():
    """Auto-generated function: testToStrMinutelyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndYearDay():
    """Auto-generated function: testToStrMinutelyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrMinutelyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekNo():
    """Auto-generated function: testToStrMinutelyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrMinutelyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrMinutelyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrMinutelyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrMinutelyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByEaster():
    """Auto-generated function: testToStrMinutelyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByEasterPos():
    """Auto-generated function: testToStrMinutelyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByEasterNeg():
    """Auto-generated function: testToStrMinutelyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByHour():
    """Auto-generated function: testToStrMinutelyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMinute():
    """Auto-generated function: testToStrMinutelyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyBySecond():
    """Auto-generated function: testToStrMinutelyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByHourAndMinute():
    """Auto-generated function: testToStrMinutelyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByHourAndSecond():
    """Auto-generated function: testToStrMinutelyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByMinuteAndSecond():
    """Auto-generated function: testToStrMinutelyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrMinutelyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrMinutelyBySetPos():
    """Auto-generated function: testToStrMinutelyBySetPos"""
    try:
        response = dateutil.RRuleTest.testToStrMinutelyBySetPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondly():
    """Auto-generated function: testToStrSecondly"""
    try:
        response = dateutil.RRuleTest.testToStrSecondly()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyInterval():
    """Auto-generated function: testToStrSecondlyInterval"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyInterval()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyIntervalLarge():
    """Auto-generated function: testToStrSecondlyIntervalLarge"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyIntervalLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonth():
    """Auto-generated function: testToStrSecondlyByMonth"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonth()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthDay():
    """Auto-generated function: testToStrSecondlyByMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndMonthDay():
    """Auto-generated function: testToStrSecondlyByMonthAndMonthDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndMonthDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekDay():
    """Auto-generated function: testToStrSecondlyByWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByNWeekDay():
    """Auto-generated function: testToStrSecondlyByNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndWeekDay():
    """Auto-generated function: testToStrSecondlyByMonthAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndNWeekDay():
    """Auto-generated function: testToStrSecondlyByMonthAndNWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndNWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthDayAndWeekDay():
    """Auto-generated function: testToStrSecondlyByMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndMonthDayAndWeekDay():
    """Auto-generated function: testToStrSecondlyByMonthAndMonthDayAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndMonthDayAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByYearDay():
    """Auto-generated function: testToStrSecondlyByYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByYearDayNeg():
    """Auto-generated function: testToStrSecondlyByYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndYearDay():
    """Auto-generated function: testToStrSecondlyByMonthAndYearDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndYearDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMonthAndYearDayNeg():
    """Auto-generated function: testToStrSecondlyByMonthAndYearDayNeg"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMonthAndYearDayNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekNo():
    """Auto-generated function: testToStrSecondlyByWeekNo"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekNo()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekNoAndWeekDay():
    """Auto-generated function: testToStrSecondlyByWeekNoAndWeekDay"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekNoAndWeekDay()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekNoAndWeekDayLarge():
    """Auto-generated function: testToStrSecondlyByWeekNoAndWeekDayLarge"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekNoAndWeekDayLarge()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekNoAndWeekDayLast():
    """Auto-generated function: testToStrSecondlyByWeekNoAndWeekDayLast"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekNoAndWeekDayLast()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByWeekNoAndWeekDay53():
    """Auto-generated function: testToStrSecondlyByWeekNoAndWeekDay53"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByWeekNoAndWeekDay53()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByEaster():
    """Auto-generated function: testToStrSecondlyByEaster"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByEaster()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByEasterPos():
    """Auto-generated function: testToStrSecondlyByEasterPos"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByEasterPos()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByEasterNeg():
    """Auto-generated function: testToStrSecondlyByEasterNeg"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByEasterNeg()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByHour():
    """Auto-generated function: testToStrSecondlyByHour"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByHour()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMinute():
    """Auto-generated function: testToStrSecondlyByMinute"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyBySecond():
    """Auto-generated function: testToStrSecondlyBySecond"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyBySecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByHourAndMinute():
    """Auto-generated function: testToStrSecondlyByHourAndMinute"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByHourAndMinute()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByHourAndSecond():
    """Auto-generated function: testToStrSecondlyByHourAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByHourAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByMinuteAndSecond():
    """Auto-generated function: testToStrSecondlyByMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByHourAndMinuteAndSecond():
    """Auto-generated function: testToStrSecondlyByHourAndMinuteAndSecond"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByHourAndMinuteAndSecond()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrSecondlyByHourAndMinuteAndSecondBug():
    """Auto-generated function: testToStrSecondlyByHourAndMinuteAndSecondBug"""
    try:
        response = dateutil.RRuleTest.testToStrSecondlyByHourAndMinuteAndSecondBug()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrWithWkSt():
    """Auto-generated function: testToStrWithWkSt"""
    try:
        response = dateutil.RRuleTest.testToStrWithWkSt()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testToStrLongIntegers():
    """Auto-generated function: testToStrLongIntegers"""
    try:
        response = dateutil.RRuleTest.testToStrLongIntegers()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testReplaceIfSet():
    """Auto-generated function: testReplaceIfSet"""
    try:
        response = dateutil.RRuleTest.testReplaceIfSet()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testReplaceIfNotSet():
    """Auto-generated function: testReplaceIfNotSet"""
    try:
        response = dateutil.RRuleTest.testReplaceIfNotSet()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_generated_aware_dtstart():
    """Auto-generated function: test_generated_aware_dtstart"""
    try:
        response = dateutil.test_generated_aware_dtstart()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_generated_aware_dtstart_rrulestr():
    """Auto-generated function: test_generated_aware_dtstart_rrulestr"""
    try:
        response = dateutil.test_generated_aware_dtstart_rrulestr()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSet():
    """Auto-generated function: testSet"""
    try:
        response = dateutil.RRuleSetTest.testSet()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetDate():
    """Auto-generated function: testSetDate"""
    try:
        response = dateutil.RRuleSetTest.testSetDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetExRule():
    """Auto-generated function: testSetExRule"""
    try:
        response = dateutil.RRuleSetTest.testSetExRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetExDate():
    """Auto-generated function: testSetExDate"""
    try:
        response = dateutil.RRuleSetTest.testSetExDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetExDateRevOrder():
    """Auto-generated function: testSetExDateRevOrder"""
    try:
        response = dateutil.RRuleSetTest.testSetExDateRevOrder()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetDateAndExDate():
    """Auto-generated function: testSetDateAndExDate"""
    try:
        response = dateutil.RRuleSetTest.testSetDateAndExDate()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetDateAndExRule():
    """Auto-generated function: testSetDateAndExRule"""
    try:
        response = dateutil.RRuleSetTest.testSetDateAndExRule()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetCount():
    """Auto-generated function: testSetCount"""
    try:
        response = dateutil.RRuleSetTest.testSetCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetCachePre():
    """Auto-generated function: testSetCachePre"""
    try:
        response = dateutil.RRuleSetTest.testSetCachePre()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetCachePost():
    """Auto-generated function: testSetCachePost"""
    try:
        response = dateutil.RRuleSetTest.testSetCachePost()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetCachePostInternal():
    """Auto-generated function: testSetCachePostInternal"""
    try:
        response = dateutil.RRuleSetTest.testSetCachePostInternal()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetRRuleCount():
    """Auto-generated function: testSetRRuleCount"""
    try:
        response = dateutil.RRuleSetTest.testSetRRuleCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetRDateCount():
    """Auto-generated function: testSetRDateCount"""
    try:
        response = dateutil.RRuleSetTest.testSetRDateCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetExRuleCount():
    """Auto-generated function: testSetExRuleCount"""
    try:
        response = dateutil.RRuleSetTest.testSetExRuleCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testSetExDateCount():
    """Auto-generated function: testSetExDateCount"""
    try:
        response = dateutil.RRuleSetTest.testSetExDateCount()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testInvalidNthWeekday():
    """Auto-generated function: testInvalidNthWeekday"""
    try:
        response = dateutil.WeekdayTest.testInvalidNthWeekday()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekdayCallable():
    """Auto-generated function: testWeekdayCallable"""
    try:
        response = dateutil.WeekdayTest.testWeekdayCallable()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekdayEquality():
    """Auto-generated function: testWeekdayEquality"""
    try:
        response = dateutil.WeekdayTest.testWeekdayEquality()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekdayEqualitySubclass():
    """Auto-generated function: testWeekdayEqualitySubclass"""
    try:
        response = dateutil.WeekdayTest.testWeekdayEqualitySubclass()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekdayReprNoN():
    """Auto-generated function: testWeekdayReprNoN"""
    try:
        response = dateutil.WeekdayTest.testWeekdayReprNoN()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def testWeekdayReprWithN():
    """Auto-generated function: testWeekdayReprWithN"""
    try:
        response = dateutil.WeekdayTest.testWeekdayReprWithN()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def clean_import():
    """Auto-generated function: clean_import"""
    try:
        response = dateutil.clean_import()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_lazy_import(clean_import, module):
    """Auto-generated function: test_lazy_import"""
    try:
        response = dateutil.test_lazy_import(clean_import, module)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_version_str():
    """Auto-generated function: test_import_version_str"""
    try:
        response = dateutil.test_import_version_str()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_version_root():
    """Auto-generated function: test_import_version_root"""
    try:
        response = dateutil.test_import_version_root()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_easter_direct():
    """Auto-generated function: test_import_easter_direct"""
    try:
        response = dateutil.test_import_easter_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_easter_from():
    """Auto-generated function: test_import_easter_from"""
    try:
        response = dateutil.test_import_easter_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_easter_start():
    """Auto-generated function: test_import_easter_start"""
    try:
        response = dateutil.test_import_easter_start()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_parser_direct():
    """Auto-generated function: test_import_parser_direct"""
    try:
        response = dateutil.test_import_parser_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_parser_from():
    """Auto-generated function: test_import_parser_from"""
    try:
        response = dateutil.test_import_parser_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_parser_all():
    """Auto-generated function: test_import_parser_all"""
    try:
        response = dateutil.test_import_parser_all()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_relative_delta_direct():
    """Auto-generated function: test_import_relative_delta_direct"""
    try:
        response = dateutil.test_import_relative_delta_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_relative_delta_from():
    """Auto-generated function: test_import_relative_delta_from"""
    try:
        response = dateutil.test_import_relative_delta_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_relative_delta_all():
    """Auto-generated function: test_import_relative_delta_all"""
    try:
        response = dateutil.test_import_relative_delta_all()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_rrule_direct():
    """Auto-generated function: test_import_rrule_direct"""
    try:
        response = dateutil.test_import_rrule_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_rrule_from():
    """Auto-generated function: test_import_rrule_from"""
    try:
        response = dateutil.test_import_rrule_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_rrule_all():
    """Auto-generated function: test_import_rrule_all"""
    try:
        response = dateutil.test_import_rrule_all()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tztest_direct():
    """Auto-generated function: test_import_tztest_direct"""
    try:
        response = dateutil.test_import_tztest_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tz_from():
    """Auto-generated function: test_import_tz_from"""
    try:
        response = dateutil.test_import_tz_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tz_all():
    """Auto-generated function: test_import_tz_all"""
    try:
        response = dateutil.test_import_tz_all()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tz_windows_direct():
    """Auto-generated function: test_import_tz_windows_direct"""
    try:
        response = dateutil.test_import_tz_windows_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tz_windows_from():
    """Auto-generated function: test_import_tz_windows_from"""
    try:
        response = dateutil.test_import_tz_windows_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_tz_windows_star():
    """Auto-generated function: test_import_tz_windows_star"""
    try:
        response = dateutil.test_import_tz_windows_star()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_zone_info_direct():
    """Auto-generated function: test_import_zone_info_direct"""
    try:
        response = dateutil.test_import_zone_info_direct()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_zone_info_from():
    """Auto-generated function: test_import_zone_info_from"""
    try:
        response = dateutil.test_import_zone_info_from()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_import_zone_info_star():
    """Auto-generated function: test_import_zone_info_star"""
    try:
        response = dateutil.test_import_zone_info_star()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_year_only(dt):
    """Auto-generated function: test_year_only"""
    try:
        response = dateutil.test_year_only(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_year_month(dt):
    """Auto-generated function: test_year_month"""
    try:
        response = dateutil.test_year_month(dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_year_month_day(dt, fmt):
    """Auto-generated function: test_year_month_day"""
    try:
        response = dateutil.test_year_month_day(dt, fmt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ymd_h(dt, date_fmt, tzoffset):
    """Auto-generated function: test_ymd_h"""
    try:
        response = dateutil.test_ymd_h(dt, date_fmt, tzoffset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ymd_hm(dt, date_fmt, time_fmt, tzoffset):
    """Auto-generated function: test_ymd_hm"""
    try:
        response = dateutil.test_ymd_hm(dt, date_fmt, time_fmt, tzoffset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ymd_hms(dt, date_fmt, time_fmt, tzoffset):
    """Auto-generated function: test_ymd_hms"""
    try:
        response = dateutil.test_ymd_hms(dt, date_fmt, time_fmt, tzoffset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_ymd_hms_micro(dt, date_fmt, time_fmt, tzoffset, precision):
    """Auto-generated function: test_ymd_hms_micro"""
    try:
        response = dateutil.test_ymd_hms_micro(dt, date_fmt, time_fmt, tzoffset, precision)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_extra_subsecond_digits(dt_str):
    """Auto-generated function: test_extra_subsecond_digits"""
    try:
        response = dateutil.test_extra_subsecond_digits(dt_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_full_tzoffsets(tzoffset):
    """Auto-generated function: test_full_tzoffsets"""
    try:
        response = dateutil.test_full_tzoffsets(tzoffset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_datetime_midnight(dt_str):
    """Auto-generated function: test_datetime_midnight"""
    try:
        response = dateutil.test_datetime_midnight(dt_str)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isoparse_sep_none(datestr, sep):
    """Auto-generated function: test_isoparse_sep_none"""
    try:
        response = dateutil.test_isoparse_sep_none(datestr, sep)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isoweek(isocal, dt_expected):
    """Auto-generated function: test_isoweek"""
    try:
        response = dateutil.test_isoweek(isocal, dt_expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isoweek_day(isocal, dt_expected):
    """Auto-generated function: test_isoweek_day"""
    try:
        response = dateutil.test_isoweek_day(isocal, dt_expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_iso_ordinal(isoord, dt_expected):
    """Auto-generated function: test_iso_ordinal"""
    try:
        response = dateutil.test_iso_ordinal(isoord, dt_expected)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_bytes(isostr, dt):
    """Auto-generated function: test_bytes"""
    try:
        response = dateutil.test_bytes(isostr, dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_iso_raises(isostr, exception):
    """Auto-generated function: test_iso_raises"""
    try:
        response = dateutil.test_iso_raises(isostr, exception)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_iso_with_sep_raises(sep_act, valid_sep, exception):
    """Auto-generated function: test_iso_with_sep_raises"""
    try:
        response = dateutil.test_iso_with_sep_raises(sep_act, valid_sep, exception)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isoparser_invalid_sep(sep):
    """Auto-generated function: test_isoparser_invalid_sep"""
    try:
        response = dateutil.test_isoparser_invalid_sep(sep)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isoparser_byte_sep():
    """Auto-generated function: test_isoparser_byte_sep"""
    try:
        response = dateutil.test_isoparser_byte_sep()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_tzstr(tzoffset):
    """Auto-generated function: test_parse_tzstr"""
    try:
        response = dateutil.test_parse_tzstr(tzoffset)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_tzstr_zero_as_utc(tzstr, zero_as_utc):
    """Auto-generated function: test_parse_tzstr_zero_as_utc"""
    try:
        response = dateutil.test_parse_tzstr_zero_as_utc(tzstr, zero_as_utc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_tzstr_fails(tzstr, exception):
    """Auto-generated function: test_parse_tzstr_fails"""
    try:
        response = dateutil.test_parse_tzstr_fails(tzstr, exception)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_isodate(d, dt_fmt, as_bytes):
    """Auto-generated function: test_parse_isodate"""
    try:
        response = dateutil.test_parse_isodate(d, dt_fmt, as_bytes)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isodate_raises(isostr, exception):
    """Auto-generated function: test_isodate_raises"""
    try:
        response = dateutil.test_isodate_raises(isostr, exception)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parse_isodate_error_text():
    """Auto-generated function: test_parse_isodate_error_text"""
    try:
        response = dateutil.test_parse_isodate_error_text()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isotime(time_val, time_fmt, as_bytes):
    """Auto-generated function: test_isotime"""
    try:
        response = dateutil.test_isotime(time_val, time_fmt, as_bytes)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isotime_midnight(isostr):
    """Auto-generated function: test_isotime_midnight"""
    try:
        response = dateutil.test_isotime_midnight(isostr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_isotime_raises(isostr, exception):
    """Auto-generated function: test_isotime_raises"""
    try:
        response = dateutil.test_isotime_raises(isostr, exception)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_YMD_could_be_day():
    """Auto-generated function: test_YMD_could_be_day"""
    try:
        response = dateutil.test_YMD_could_be_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parser_private_warns():
    """Auto-generated function: test_parser_private_warns"""
    try:
        response = dateutil.test_parser_private_warns()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_parser_parser_private_not_warns():
    """Auto-generated function: test_parser_parser_private_not_warns"""
    try:
        response = dateutil.test_parser_parser_private_not_warns()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_tzstr_internal_timedeltas():
    """Auto-generated function: test_tzstr_internal_timedeltas"""
    try:
        response = dateutil.test_tzstr_internal_timedeltas()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_timespec_auto(dt, sep):
    """Auto-generated function: test_timespec_auto"""
    try:
        response = dateutil.test_isoparse_prop.test_timespec_auto(dt, sep)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_gettz_returns_local(gettz_arg, dt):
    """Auto-generated function: test_gettz_returns_local"""
    try:
        response = dateutil.test_tz_prop.test_gettz_returns_local(gettz_arg, dt)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_convertyear(n):
    """Auto-generated function: test_convertyear"""
    try:
        response = dateutil.test_parser_prop.test_convertyear(n)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_convertyear_no_specified_century(n):
    """Auto-generated function: test_convertyear_no_specified_century"""
    try:
        response = dateutil.test_parser_prop.test_convertyear_no_specified_century(n)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calculate_sha512(fpath):
    """Auto-generated function: calculate_sha512"""
    try:
        response = dateutil.ci_tools.make_zonefile_metadata.calculate_sha512(fpath)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def pointer_mock():
    """Auto-generated function: pointer_mock"""
    try:
        response = dateutil.docs.conf.pointer_mock()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_mlk_day():
    """Auto-generated function: test_mlk_day"""
    try:
        response = dateutil.docs.exercises.solutions.mlk_day_rrule_solution.test_mlk_day()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/main', methods=['POST'])
def call_main():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    metadata_file = request_json.get("metadata_file")
    

    return main(metadata_file)

@app.route('/run', methods=['POST'])
def call_run():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return run()

@app.route('/README', methods=['POST'])
def call_README():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return README()

@app.route('/easter', methods=['POST'])
def call_easter():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    method = request_json.get("method")
    

    return easter(year, method)

@app.route('/today', methods=['POST'])
def call_today():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzinfo = request_json.get("tzinfo")
    

    return today(tzinfo)

@app.route('/default_tzinfo', methods=['POST'])
def call_default_tzinfo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    tzinfo = request_json.get("tzinfo")
    

    return default_tzinfo(dt, tzinfo)

@app.route('/within_delta', methods=['POST'])
def call_within_delta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt1 = request_json.get("dt1")
    
    dt2 = request_json.get("dt2")
    
    delta = request_json.get("delta")
    

    return within_delta(dt1, dt2, delta)

@app.route('/weeks', methods=['POST'])
def call_weeks():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    value = request_json.get("value")
    

    return weeks(value)

@app.route('/normalized', methods=['POST'])
def call_normalized():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return normalized()

@app.route('/count', methods=['POST'])
def call_count():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return count()

@app.route('/before', methods=['POST'])
def call_before():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    inc = request_json.get("inc")
    

    return before(dt, inc)

@app.route('/after', methods=['POST'])
def call_after():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    inc = request_json.get("inc")
    

    return after(dt, inc)

@app.route('/xafter', methods=['POST'])
def call_xafter():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    count = request_json.get("count")
    
    inc = request_json.get("inc")
    

    return xafter(dt, count, inc)

@app.route('/between', methods=['POST'])
def call_between():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    after = request_json.get("after")
    
    before = request_json.get("before")
    
    inc = request_json.get("inc")
    
    count = request_json.get("count")
    

    return between(after, before, inc, count)

@app.route('/replace', methods=['POST'])
def call_replace():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return replace()

@app.route('/rebuild', methods=['POST'])
def call_rebuild():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    

    return rebuild(year, month)

@app.route('/ydayset', methods=['POST'])
def call_ydayset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    
    day = request_json.get("day")
    

    return ydayset(year, month, day)

@app.route('/mdayset', methods=['POST'])
def call_mdayset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    
    day = request_json.get("day")
    

    return mdayset(year, month, day)

@app.route('/wdayset', methods=['POST'])
def call_wdayset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    
    day = request_json.get("day")
    

    return wdayset(year, month, day)

@app.route('/ddayset', methods=['POST'])
def call_ddayset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    
    day = request_json.get("day")
    

    return ddayset(year, month, day)

@app.route('/htimeset', methods=['POST'])
def call_htimeset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    hour = request_json.get("hour")
    
    minute = request_json.get("minute")
    
    second = request_json.get("second")
    

    return htimeset(hour, minute, second)

@app.route('/mtimeset', methods=['POST'])
def call_mtimeset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    hour = request_json.get("hour")
    
    minute = request_json.get("minute")
    
    second = request_json.get("second")
    

    return mtimeset(hour, minute, second)

@app.route('/stimeset', methods=['POST'])
def call_stimeset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    hour = request_json.get("hour")
    
    minute = request_json.get("minute")
    
    second = request_json.get("second")
    

    return stimeset(hour, minute, second)

@app.route('/rrule', methods=['POST'])
def call_rrule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    rrule = request_json.get("rrule")
    

    return rrule(rrule)

@app.route('/rdate', methods=['POST'])
def call_rdate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    rdate = request_json.get("rdate")
    

    return rdate(rdate)

@app.route('/exrule', methods=['POST'])
def call_exrule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    exrule = request_json.get("exrule")
    

    return exrule(exrule)

@app.route('/exdate', methods=['POST'])
def call_exdate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    exdate = request_json.get("exdate")
    

    return exdate(exdate)

@app.route('/instance', methods=['POST'])
def call_instance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    

    return instance(cls)

@app.route('/tzname_in_python2', methods=['POST'])
def call_tzname_in_python2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    namefunc = request_json.get("namefunc")
    

    return tzname_in_python2(namefunc)

@app.route('/is_ambiguous', methods=['POST'])
def call_is_ambiguous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return is_ambiguous(dt)

@app.route('/fromutc', methods=['POST'])
def call_fromutc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return fromutc(dt)

@app.route('/utcoffset', methods=['POST'])
def call_utcoffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return utcoffset(dt)

@app.route('/dst', methods=['POST'])
def call_dst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return dst(dt)

@app.route('/tzname', methods=['POST'])
def call_tzname():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return tzname(dt)

@app.route('/utcoffset', methods=['POST'])
def call_utcoffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return utcoffset(dt)

@app.route('/dst', methods=['POST'])
def call_dst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return dst(dt)

@app.route('/tzname', methods=['POST'])
def call_tzname():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return tzname(dt)

@app.route('/is_ambiguous', methods=['POST'])
def call_is_ambiguous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    idx = request_json.get("idx")
    

    return is_ambiguous(dt, idx)

@app.route('/fromutc', methods=['POST'])
def call_fromutc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return fromutc(dt)

@app.route('/transitions', methods=['POST'])
def call_transitions():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    

    return transitions(year)

@app.route('/keys', methods=['POST'])
def call_keys():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return keys()

@app.route('/get', methods=['POST'])
def call_get():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzid = request_json.get("tzid")
    

    return get(tzid)

@app.route('/datetime_exists', methods=['POST'])
def call_datetime_exists():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    tz = request_json.get("tz")
    

    return datetime_exists(dt, tz)

@app.route('/datetime_ambiguous', methods=['POST'])
def call_datetime_ambiguous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    tz = request_json.get("tz")
    

    return datetime_ambiguous(dt, tz)

@app.route('/resolve_imaginary', methods=['POST'])
def call_resolve_imaginary():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return resolve_imaginary(dt)

@app.route('/load_name', methods=['POST'])
def call_load_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    offset = request_json.get("offset")
    

    return load_name(offset)

@app.route('/name_from_string', methods=['POST'])
def call_name_from_string():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzname_str = request_json.get("tzname_str")
    

    return name_from_string(tzname_str)

@app.route('/list', methods=['POST'])
def call_list():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return list()

@app.route('/display', methods=['POST'])
def call_display():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return display()

@app.route('/transitions', methods=['POST'])
def call_transitions():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    

    return transitions(year)

@app.route('/picknthweekday', methods=['POST'])
def call_picknthweekday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    month = request_json.get("month")
    
    dayofweek = request_json.get("dayofweek")
    
    hour = request_json.get("hour")
    
    minute = request_json.get("minute")
    
    whichweek = request_json.get("whichweek")
    

    return picknthweekday(year, month, dayofweek, hour, minute, whichweek)

@app.route('/valuestodict', methods=['POST'])
def call_valuestodict():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    key = request_json.get("key")
    

    return valuestodict(key)

@app.route('/isoparse', methods=['POST'])
def call_isoparse():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt_str = request_json.get("dt_str")
    

    return isoparse(dt_str)

@app.route('/parse_isodate', methods=['POST'])
def call_parse_isodate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    datestr = request_json.get("datestr")
    

    return parse_isodate(datestr)

@app.route('/parse_isotime', methods=['POST'])
def call_parse_isotime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    timestr = request_json.get("timestr")
    

    return parse_isotime(timestr)

@app.route('/parse_tzstr', methods=['POST'])
def call_parse_tzstr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzstr = request_json.get("tzstr")
    
    zero_as_utc = request_json.get("zero_as_utc")
    

    return parse_tzstr(tzstr, zero_as_utc)

@app.route('/get_token', methods=['POST'])
def call_get_token():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return get_token()

@app.route('/next', methods=['POST'])
def call_next():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return next()

@app.route('/split', methods=['POST'])
def call_split():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    
    s = request_json.get("s")
    

    return split(cls, s)

@app.route('/isword', methods=['POST'])
def call_isword():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    
    nextchar = request_json.get("nextchar")
    

    return isword(cls, nextchar)

@app.route('/isnum', methods=['POST'])
def call_isnum():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    
    nextchar = request_json.get("nextchar")
    

    return isnum(cls, nextchar)

@app.route('/isspace', methods=['POST'])
def call_isspace():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    
    nextchar = request_json.get("nextchar")
    

    return isspace(cls, nextchar)

@app.route('/jump', methods=['POST'])
def call_jump():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return jump(name)

@app.route('/weekday', methods=['POST'])
def call_weekday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return weekday(name)

@app.route('/month', methods=['POST'])
def call_month():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return month(name)

@app.route('/hms', methods=['POST'])
def call_hms():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return hms(name)

@app.route('/ampm', methods=['POST'])
def call_ampm():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return ampm(name)

@app.route('/pertain', methods=['POST'])
def call_pertain():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return pertain(name)

@app.route('/utczone', methods=['POST'])
def call_utczone():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return utczone(name)

@app.route('/tzoffset', methods=['POST'])
def call_tzoffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return tzoffset(name)

@app.route('/convertyear', methods=['POST'])
def call_convertyear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    year = request_json.get("year")
    
    century_specified = request_json.get("century_specified")
    

    return convertyear(year, century_specified)

@app.route('/validate', methods=['POST'])
def call_validate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    res = request_json.get("res")
    

    return validate(res)

@app.route('/has_year', methods=['POST'])
def call_has_year():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return has_year()

@app.route('/has_month', methods=['POST'])
def call_has_month():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return has_month()

@app.route('/has_day', methods=['POST'])
def call_has_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return has_day()

@app.route('/could_be_day', methods=['POST'])
def call_could_be_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    value = request_json.get("value")
    

    return could_be_day(value)

@app.route('/append', methods=['POST'])
def call_append():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    val = request_json.get("val")
    
    label = request_json.get("label")
    

    return append(val, label)

@app.route('/resolve_ymd', methods=['POST'])
def call_resolve_ymd():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    yearfirst = request_json.get("yearfirst")
    
    dayfirst = request_json.get("dayfirst")
    

    return resolve_ymd(yearfirst, dayfirst)

@app.route('/parse', methods=['POST'])
def call_parse():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzstr = request_json.get("tzstr")
    

    return parse(tzstr)

@app.route('/rebuild', methods=['POST'])
def call_rebuild():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    filename = request_json.get("filename")
    
    tag = request_json.get("tag")
    
    format = request_json.get("format")
    
    zonegroups = request_json.get("zonegroups")
    
    metadata = request_json.get("metadata")
    

    return rebuild(filename, tag, format, zonegroups, metadata)

@app.route('/getzoneinfofile_stream', methods=['POST'])
def call_getzoneinfofile_stream():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return getzoneinfofile_stream()

@app.route('/get', methods=['POST'])
def call_get():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    
    default = request_json.get("default")
    

    return get(name, default)

@app.route('/get_zonefile_instance', methods=['POST'])
def call_get_zonefile_instance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    new_instance = request_json.get("new_instance")
    

    return get_zonefile_instance(new_instance)

@app.route('/gettz', methods=['POST'])
def call_gettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return gettz(name)

@app.route('/gettz_db_metadata', methods=['POST'])
def call_gettz_db_metadata():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return gettz_db_metadata()

@app.route('/testInheritance', methods=['POST'])
def call_testInheritance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInheritance()

@app.route('/testMonthEndMonthBeginning', methods=['POST'])
def call_testMonthEndMonthBeginning():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthEndMonthBeginning()

@app.route('/testMonthEndMonthBeginningLeapYear', methods=['POST'])
def call_testMonthEndMonthBeginningLeapYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthEndMonthBeginningLeapYear()

@app.route('/testNextMonth', methods=['POST'])
def call_testNextMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextMonth()

@app.route('/testNextMonthPlusOneWeek', methods=['POST'])
def call_testNextMonthPlusOneWeek():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextMonthPlusOneWeek()

@app.route('/testNextMonthPlusOneWeek10am', methods=['POST'])
def call_testNextMonthPlusOneWeek10am():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextMonthPlusOneWeek10am()

@app.route('/testNextMonthPlusOneWeek10amDiff', methods=['POST'])
def call_testNextMonthPlusOneWeek10amDiff():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextMonthPlusOneWeek10amDiff()

@app.route('/testOneMonthBeforeOneYear', methods=['POST'])
def call_testOneMonthBeforeOneYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testOneMonthBeforeOneYear()

@app.route('/testMonthsOfDiffNumOfDays', methods=['POST'])
def call_testMonthsOfDiffNumOfDays():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthsOfDiffNumOfDays()

@app.route('/testMonthsOfDiffNumOfDaysWithYears', methods=['POST'])
def call_testMonthsOfDiffNumOfDaysWithYears():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthsOfDiffNumOfDaysWithYears()

@app.route('/testNextFriday', methods=['POST'])
def call_testNextFriday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextFriday()

@app.route('/testNextFridayInt', methods=['POST'])
def call_testNextFridayInt():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextFridayInt()

@app.route('/testLastFridayInThisMonth', methods=['POST'])
def call_testLastFridayInThisMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLastFridayInThisMonth()

@app.route('/testLastDayOfFebruary', methods=['POST'])
def call_testLastDayOfFebruary():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLastDayOfFebruary()

@app.route('/testLastDayOfFebruaryLeapYear', methods=['POST'])
def call_testLastDayOfFebruaryLeapYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLastDayOfFebruaryLeapYear()

@app.route('/testNextWednesdayIsToday', methods=['POST'])
def call_testNextWednesdayIsToday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextWednesdayIsToday()

@app.route('/testNextWednesdayNotToday', methods=['POST'])
def call_testNextWednesdayNotToday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNextWednesdayNotToday()

@app.route('/testAddMoreThan12Months', methods=['POST'])
def call_testAddMoreThan12Months():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAddMoreThan12Months()

@app.route('/testAddNegativeMonths', methods=['POST'])
def call_testAddNegativeMonths():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAddNegativeMonths()

@app.route('/test15thISOYearWeek', methods=['POST'])
def call_test15thISOYearWeek():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test15thISOYearWeek()

@app.route('/testMillenniumAge', methods=['POST'])
def call_testMillenniumAge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMillenniumAge()

@app.route('/testJohnAge', methods=['POST'])
def call_testJohnAge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testJohnAge()

@app.route('/testJohnAgeWithDate', methods=['POST'])
def call_testJohnAgeWithDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testJohnAgeWithDate()

@app.route('/testYearDay', methods=['POST'])
def call_testYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearDay()

@app.route('/testYearDayBug', methods=['POST'])
def call_testYearDayBug():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearDayBug()

@app.route('/testNonLeapYearDay', methods=['POST'])
def call_testNonLeapYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNonLeapYearDay()

@app.route('/testAddition', methods=['POST'])
def call_testAddition():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAddition()

@app.route('/testAbsoluteAddition', methods=['POST'])
def call_testAbsoluteAddition():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAbsoluteAddition()

@app.route('/testAdditionToDatetime', methods=['POST'])
def call_testAdditionToDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAdditionToDatetime()

@app.route('/testRightAdditionToDatetime', methods=['POST'])
def call_testRightAdditionToDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRightAdditionToDatetime()

@app.route('/testAdditionInvalidType', methods=['POST'])
def call_testAdditionInvalidType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAdditionInvalidType()

@app.route('/testAdditionUnsupportedType', methods=['POST'])
def call_testAdditionUnsupportedType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAdditionUnsupportedType()

@app.route('/testAdditionFloatValue', methods=['POST'])
def call_testAdditionFloatValue():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAdditionFloatValue()

@app.route('/testAdditionFloatFractionals', methods=['POST'])
def call_testAdditionFloatFractionals():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAdditionFloatFractionals()

@app.route('/testSubtraction', methods=['POST'])
def call_testSubtraction():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSubtraction()

@app.route('/testRightSubtractionFromDatetime', methods=['POST'])
def call_testRightSubtractionFromDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRightSubtractionFromDatetime()

@app.route('/testSubractionWithDatetime', methods=['POST'])
def call_testSubractionWithDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSubractionWithDatetime()

@app.route('/testSubtractionInvalidType', methods=['POST'])
def call_testSubtractionInvalidType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSubtractionInvalidType()

@app.route('/testSubtractionUnsupportedType', methods=['POST'])
def call_testSubtractionUnsupportedType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSubtractionUnsupportedType()

@app.route('/testMultiplication', methods=['POST'])
def call_testMultiplication():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiplication()

@app.route('/testMultiplicationUnsupportedType', methods=['POST'])
def call_testMultiplicationUnsupportedType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiplicationUnsupportedType()

@app.route('/testDivision', methods=['POST'])
def call_testDivision():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDivision()

@app.route('/testDivisionUnsupportedType', methods=['POST'])
def call_testDivisionUnsupportedType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDivisionUnsupportedType()

@app.route('/testBoolean', methods=['POST'])
def call_testBoolean():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBoolean()

@app.route('/testAbsoluteValueNegative', methods=['POST'])
def call_testAbsoluteValueNegative():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAbsoluteValueNegative()

@app.route('/testAbsoluteValuePositive', methods=['POST'])
def call_testAbsoluteValuePositive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAbsoluteValuePositive()

@app.route('/testComparison', methods=['POST'])
def call_testComparison():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testComparison()

@app.route('/testInequalityTypeMismatch', methods=['POST'])
def call_testInequalityTypeMismatch():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityTypeMismatch()

@app.route('/testInequalityUnsupportedType', methods=['POST'])
def call_testInequalityUnsupportedType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityUnsupportedType()

@app.route('/testInequalityWeekdays', methods=['POST'])
def call_testInequalityWeekdays():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityWeekdays()

@app.route('/testMonthOverflow', methods=['POST'])
def call_testMonthOverflow():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthOverflow()

@app.route('/testWeeks', methods=['POST'])
def call_testWeeks():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeks()

@app.route('/testRelativeDeltaRepr', methods=['POST'])
def call_testRelativeDeltaRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaRepr()

@app.route('/testRelativeDeltaFractionalYear', methods=['POST'])
def call_testRelativeDeltaFractionalYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalYear()

@app.route('/testRelativeDeltaFractionalMonth', methods=['POST'])
def call_testRelativeDeltaFractionalMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalMonth()

@app.route('/testRelativeDeltaInvalidDatetimeObject', methods=['POST'])
def call_testRelativeDeltaInvalidDatetimeObject():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaInvalidDatetimeObject()

@app.route('/testRelativeDeltaFractionalAbsolutes', methods=['POST'])
def call_testRelativeDeltaFractionalAbsolutes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalAbsolutes()

@app.route('/testRelativeDeltaFractionalRepr', methods=['POST'])
def call_testRelativeDeltaFractionalRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalRepr()

@app.route('/testRelativeDeltaFractionalWeeks', methods=['POST'])
def call_testRelativeDeltaFractionalWeeks():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalWeeks()

@app.route('/testRelativeDeltaFractionalDays', methods=['POST'])
def call_testRelativeDeltaFractionalDays():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalDays()

@app.route('/testRelativeDeltaFractionalHours', methods=['POST'])
def call_testRelativeDeltaFractionalHours():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalHours()

@app.route('/testRelativeDeltaFractionalMinutes', methods=['POST'])
def call_testRelativeDeltaFractionalMinutes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalMinutes()

@app.route('/testRelativeDeltaFractionalSeconds', methods=['POST'])
def call_testRelativeDeltaFractionalSeconds():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalSeconds()

@app.route('/testRelativeDeltaFractionalPositiveOverflow', methods=['POST'])
def call_testRelativeDeltaFractionalPositiveOverflow():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalPositiveOverflow()

@app.route('/testRelativeDeltaFractionalNegativeDays', methods=['POST'])
def call_testRelativeDeltaFractionalNegativeDays():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalNegativeDays()

@app.route('/testRelativeDeltaNormalizeFractionalDays', methods=['POST'])
def call_testRelativeDeltaNormalizeFractionalDays():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaNormalizeFractionalDays()

@app.route('/testRelativeDeltaNormalizeFractionalDays2', methods=['POST'])
def call_testRelativeDeltaNormalizeFractionalDays2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaNormalizeFractionalDays2()

@app.route('/testRelativeDeltaNormalizeFractionalMinutes', methods=['POST'])
def call_testRelativeDeltaNormalizeFractionalMinutes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaNormalizeFractionalMinutes()

@app.route('/testRelativeDeltaNormalizeFractionalSeconds', methods=['POST'])
def call_testRelativeDeltaNormalizeFractionalSeconds():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaNormalizeFractionalSeconds()

@app.route('/testRelativeDeltaFractionalPositiveOverflow2', methods=['POST'])
def call_testRelativeDeltaFractionalPositiveOverflow2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalPositiveOverflow2()

@app.route('/testRelativeDeltaFractionalNegativeOverflow', methods=['POST'])
def call_testRelativeDeltaFractionalNegativeOverflow():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRelativeDeltaFractionalNegativeOverflow()

@app.route('/testInvalidYearDay', methods=['POST'])
def call_testInvalidYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInvalidYearDay()

@app.route('/testAddTimedeltaToUnpopulatedRelativedelta', methods=['POST'])
def call_testAddTimedeltaToUnpopulatedRelativedelta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAddTimedeltaToUnpopulatedRelativedelta()

@app.route('/testAddTimedeltaToPopulatedRelativeDelta', methods=['POST'])
def call_testAddTimedeltaToPopulatedRelativeDelta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAddTimedeltaToPopulatedRelativeDelta()

@app.route('/testHashable', methods=['POST'])
def call_testHashable():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHashable()

@app.route('/testDayOfMonthPlus', methods=['POST'])
def call_testDayOfMonthPlus():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDayOfMonthPlus()

@app.route('/testLastDayOfMonthPlus', methods=['POST'])
def call_testLastDayOfMonthPlus():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLastDayOfMonthPlus()

@app.route('/testDayOfMonthMinus', methods=['POST'])
def call_testDayOfMonthMinus():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDayOfMonthMinus()

@app.route('/testLastDayOfMonthMinus', methods=['POST'])
def call_testLastDayOfMonthMinus():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLastDayOfMonthMinus()

@app.route('/test_one_day', methods=['POST'])
def call_test_one_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_one_day()

@app.route('/test_minus_one_day', methods=['POST'])
def call_test_minus_one_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_minus_one_day()

@app.route('/test_height_days', methods=['POST'])
def call_test_height_days():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_height_days()

@app.route('/test_minus_height_days', methods=['POST'])
def call_test_minus_height_days():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_minus_height_days()

@app.route('/test_one_day_set_one_week', methods=['POST'])
def call_test_one_day_set_one_week():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_one_day_set_one_week()

@app.route('/test_minus_one_day_set_one_week', methods=['POST'])
def call_test_minus_one_day_set_one_week():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_minus_one_day_set_one_week()

@app.route('/test_height_days_set_minus_one_week', methods=['POST'])
def call_test_height_days_set_minus_one_week():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_height_days_set_minus_one_week()

@app.route('/test_minus_height_days_set_minus_one_week', methods=['POST'])
def call_test_minus_height_days_set_minus_one_week():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_minus_height_days_set_minus_one_week()

@app.route('/pytest_collection_modifyitems', methods=['POST'])
def call_pytest_collection_modifyitems():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    items = request_json.get("items")
    

    return pytest_collection_modifyitems(items)

@app.route('/set_tzpath', methods=['POST'])
def call_set_tzpath():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return set_tzpath()

@app.route('/test_imported_modules', methods=['POST'])
def call_test_imported_modules():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_imported_modules()

@app.route('/test_easter_western', methods=['POST'])
def call_test_easter_western():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    easter_date = request_json.get("easter_date")
    

    return test_easter_western(easter_date)

@app.route('/test_easter_orthodox', methods=['POST'])
def call_test_easter_orthodox():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    easter_date = request_json.get("easter_date")
    

    return test_easter_orthodox(easter_date)

@app.route('/test_easter_julian', methods=['POST'])
def call_test_easter_julian():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    easter_date = request_json.get("easter_date")
    

    return test_easter_julian(easter_date)

@app.route('/test_easter_bad_method', methods=['POST'])
def call_test_easter_bad_method():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_easter_bad_method()

@app.route('/get_timezone_tuple', methods=['POST'])
def call_get_timezone_tuple():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return get_timezone_tuple(dt)

@app.route('/gettz', methods=['POST'])
def call_gettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzname = request_json.get("tzname")
    

    return gettz(tzname)

@app.route('/testFoldPositiveUTCOffset', methods=['POST'])
def call_testFoldPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFoldPositiveUTCOffset()

@app.route('/testGapPositiveUTCOffset', methods=['POST'])
def call_testGapPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGapPositiveUTCOffset()

@app.route('/testFoldNegativeUTCOffset', methods=['POST'])
def call_testFoldNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFoldNegativeUTCOffset()

@app.route('/testGapNegativeUTCOffset', methods=['POST'])
def call_testGapNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGapNegativeUTCOffset()

@app.route('/testFoldLondon', methods=['POST'])
def call_testFoldLondon():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFoldLondon()

@app.route('/testFoldIndependence', methods=['POST'])
def call_testFoldIndependence():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFoldIndependence()

@app.route('/testInZoneFoldEquality', methods=['POST'])
def call_testInZoneFoldEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInZoneFoldEquality()

@app.route('/testAmbiguousNegativeUTCOffset', methods=['POST'])
def call_testAmbiguousNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAmbiguousNegativeUTCOffset()

@app.route('/testAmbiguousPositiveUTCOffset', methods=['POST'])
def call_testAmbiguousPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAmbiguousPositiveUTCOffset()

@app.route('/testUnambiguousNegativeUTCOffset', methods=['POST'])
def call_testUnambiguousNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousNegativeUTCOffset()

@app.route('/testUnambiguousPositiveUTCOffset', methods=['POST'])
def call_testUnambiguousPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousPositiveUTCOffset()

@app.route('/testUnambiguousGapNegativeUTCOffset', methods=['POST'])
def call_testUnambiguousGapNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousGapNegativeUTCOffset()

@app.route('/testUnambiguousGapPositiveUTCOffset', methods=['POST'])
def call_testUnambiguousGapPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousGapPositiveUTCOffset()

@app.route('/testImaginaryNegativeUTCOffset', methods=['POST'])
def call_testImaginaryNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testImaginaryNegativeUTCOffset()

@app.route('/testNotImaginaryNegativeUTCOffset', methods=['POST'])
def call_testNotImaginaryNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNotImaginaryNegativeUTCOffset()

@app.route('/testImaginaryPositiveUTCOffset', methods=['POST'])
def call_testImaginaryPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testImaginaryPositiveUTCOffset()

@app.route('/testNotImaginaryPositiveUTCOffset', methods=['POST'])
def call_testNotImaginaryPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNotImaginaryPositiveUTCOffset()

@app.route('/testNotImaginaryFoldNegativeUTCOffset', methods=['POST'])
def call_testNotImaginaryFoldNegativeUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNotImaginaryFoldNegativeUTCOffset()

@app.route('/testNotImaginaryFoldPositiveUTCOffset', methods=['POST'])
def call_testNotImaginaryFoldPositiveUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNotImaginaryFoldPositiveUTCOffset()

@app.route('/testEqualAmbiguousComparison', methods=['POST'])
def call_testEqualAmbiguousComparison():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testEqualAmbiguousComparison()

@app.route('/get_args', methods=['POST'])
def call_get_args():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzname = request_json.get("tzname")
    

    return get_args(tzname)

@app.route('/get_utc_transitions', methods=['POST'])
def call_get_utc_transitions():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzi = request_json.get("tzi")
    
    year = request_json.get("year")
    
    gap = request_json.get("gap")
    

    return get_utc_transitions(tzi, year, gap)

@app.route('/testSingleton', methods=['POST'])
def call_testSingleton():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSingleton()

@app.route('/testOffset', methods=['POST'])
def call_testOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testOffset()

@app.route('/testDst', methods=['POST'])
def call_testDst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDst()

@app.route('/testTzName', methods=['POST'])
def call_testTzName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzName()

@app.route('/testEquality', methods=['POST'])
def call_testEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testEquality()

@app.route('/testInequality', methods=['POST'])
def call_testInequality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequality()

@app.route('/testInequalityInteger', methods=['POST'])
def call_testInequalityInteger():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityInteger()

@app.route('/testInequalityUnsupported', methods=['POST'])
def call_testInequalityUnsupported():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityUnsupported()

@app.route('/testRepr', methods=['POST'])
def call_testRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRepr()

@app.route('/testTimeOnlyUTC', methods=['POST'])
def call_testTimeOnlyUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyUTC()

@app.route('/testAmbiguity', methods=['POST'])
def call_testAmbiguity():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAmbiguity()

@app.route('/testTimedeltaOffset', methods=['POST'])
def call_testTimedeltaOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimedeltaOffset()

@app.route('/testTzNameNone', methods=['POST'])
def call_testTzNameNone():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzNameNone()

@app.route('/testTimeOnlyOffset', methods=['POST'])
def call_testTimeOnlyOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyOffset()

@app.route('/testTzOffsetRepr', methods=['POST'])
def call_testTzOffsetRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzOffsetRepr()

@app.route('/testUTCEquality', methods=['POST'])
def call_testUTCEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUTCEquality()

@app.route('/testInequalityInvalid', methods=['POST'])
def call_testInequalityInvalid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityInvalid()

@app.route('/testTzOffsetInstance', methods=['POST'])
def call_testTzOffsetInstance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzOffsetInstance()

@app.route('/testTzOffsetSingletonDifferent', methods=['POST'])
def call_testTzOffsetSingletonDifferent():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzOffsetSingletonDifferent()

@app.route('/test_tzoffset_weakref', methods=['POST'])
def call_test_tzoffset_weakref():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzoffset_weakref()

@app.route('/test_tzoffset_singleton', methods=['POST'])
def call_test_tzoffset_singleton():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    args = request_json.get("args")
    

    return test_tzoffset_singleton(args)

@app.route('/test_tzoffset_sub_minute', methods=['POST'])
def call_test_tzoffset_sub_minute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzoffset_sub_minute()

@app.route('/test_tzoffset_sub_minute_rounding', methods=['POST'])
def call_test_tzoffset_sub_minute_rounding():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzoffset_sub_minute_rounding()

@app.route('/testInequalityFixedOffset', methods=['POST'])
def call_testInequalityFixedOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInequalityFixedOffset()

@app.route('/test_tzoffset_is', methods=['POST'])
def call_test_tzoffset_is():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    args = request_json.get("args")
    
    kwargs = request_json.get("kwargs")
    

    return test_tzoffset_is(args, kwargs)

@app.route('/test_tzoffset_is_not', methods=['POST'])
def call_test_tzoffset_is_not():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzoffset_is_not()

@app.route('/testTzNameDST', methods=['POST'])
def call_testTzNameDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzNameDST()

@app.route('/testTzNameUTC', methods=['POST'])
def call_testTzNameUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzNameUTC()

@app.route('/testOffsetDST', methods=['POST'])
def call_testOffsetDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testOffsetDST()

@app.route('/testOffsetUTC', methods=['POST'])
def call_testOffsetUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testOffsetUTC()

@app.route('/testDSTDST', methods=['POST'])
def call_testDSTDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDSTDST()

@app.route('/testDSTUTC', methods=['POST'])
def call_testDSTUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDSTUTC()

@app.route('/testTimeOnlyOffsetLocalUTC', methods=['POST'])
def call_testTimeOnlyOffsetLocalUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyOffsetLocalUTC()

@app.route('/testTimeOnlyOffsetLocalDST', methods=['POST'])
def call_testTimeOnlyOffsetLocalDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyOffsetLocalDST()

@app.route('/testTimeOnlyDSTLocalUTC', methods=['POST'])
def call_testTimeOnlyDSTLocalUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyDSTLocalUTC()

@app.route('/testTimeOnlyDSTLocalDST', methods=['POST'])
def call_testTimeOnlyDSTLocalDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyDSTLocalDST()

@app.route('/mark_tzlocal_nix', methods=['POST'])
def call_mark_tzlocal_nix():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    f = request_json.get("f")
    

    return mark_tzlocal_nix(f)

@app.route('/test_tzlocal_utc_equal', methods=['POST'])
def call_test_tzlocal_utc_equal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzvar = request_json.get("tzvar")
    

    return test_tzlocal_utc_equal(tzvar)

@app.route('/test_tzlocal_utc_unequal', methods=['POST'])
def call_test_tzlocal_utc_unequal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzvar = request_json.get("tzvar")
    

    return test_tzlocal_utc_unequal(tzvar)

@app.route('/test_tzlocal_local_time_trim_colon', methods=['POST'])
def call_test_tzlocal_local_time_trim_colon():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzlocal_local_time_trim_colon()

@app.route('/test_tzlocal_offset_equal', methods=['POST'])
def call_test_tzlocal_offset_equal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzvar = request_json.get("tzvar")
    
    tzoff = request_json.get("tzoff")
    

    return test_tzlocal_offset_equal(tzvar, tzoff)

@app.route('/test_tzlocal_offset_unequal', methods=['POST'])
def call_test_tzlocal_offset_unequal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzvar = request_json.get("tzvar")
    
    tzoff = request_json.get("tzoff")
    

    return test_tzlocal_offset_unequal(tzvar, tzoff)

@app.route('/testGettz', methods=['POST'])
def call_testGettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGettz()

@app.route('/testGetTzEquality', methods=['POST'])
def call_testGetTzEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetTzEquality()

@app.route('/testTimeOnlyGettz', methods=['POST'])
def call_testTimeOnlyGettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyGettz()

@app.route('/testTimeOnlyGettzDST', methods=['POST'])
def call_testTimeOnlyGettzDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyGettzDST()

@app.route('/testTimeOnlyGettzTzName', methods=['POST'])
def call_testTimeOnlyGettzTzName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyGettzTzName()

@app.route('/testTimeOnlyFormatZ', methods=['POST'])
def call_testTimeOnlyFormatZ():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyFormatZ()

@app.route('/testPortugalDST', methods=['POST'])
def call_testPortugalDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPortugalDST()

@app.route('/testGettzCacheTzFile', methods=['POST'])
def call_testGettzCacheTzFile():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGettzCacheTzFile()

@app.route('/testGettzCacheTzLocal', methods=['POST'])
def call_testGettzCacheTzLocal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGettzCacheTzLocal()

@app.route('/test_gettz_same_result_for_none_and_empty_string', methods=['POST'])
def call_test_gettz_same_result_for_none_and_empty_string():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_gettz_same_result_for_none_and_empty_string()

@app.route('/test_gettz_badzone', methods=['POST'])
def call_test_gettz_badzone():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    badzone = request_json.get("badzone")
    

    return test_gettz_badzone(badzone)

@app.route('/test_gettz_badzone_unicode', methods=['POST'])
def call_test_gettz_badzone_unicode():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_gettz_badzone_unicode()

@app.route('/test_gettz_zone_wrong_type', methods=['POST'])
def call_test_gettz_zone_wrong_type():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    badzone = request_json.get("badzone")
    
    exc_reason = request_json.get("exc_reason")
    

    return test_gettz_zone_wrong_type(badzone, exc_reason)

@app.route('/test_gettz_cache_clear', methods=['POST'])
def call_test_gettz_cache_clear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_gettz_cache_clear()

@app.route('/test_gettz_set_cache_size', methods=['POST'])
def call_test_gettz_set_cache_size():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_gettz_set_cache_size()

@app.route('/test_gettz_weakref', methods=['POST'])
def call_test_gettz_weakref():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_gettz_weakref()

@app.route('/testZoneInfoFileStart1', methods=['POST'])
def call_testZoneInfoFileStart1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoFileStart1()

@app.route('/testZoneInfoFileEnd1', methods=['POST'])
def call_testZoneInfoFileEnd1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoFileEnd1()

@app.route('/testZoneInfoOffsetSignal', methods=['POST'])
def call_testZoneInfoOffsetSignal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoOffsetSignal()

@app.route('/testZoneInfoCopy', methods=['POST'])
def call_testZoneInfoCopy():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoCopy()

@app.route('/testZoneInfoDeepCopy', methods=['POST'])
def call_testZoneInfoDeepCopy():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoDeepCopy()

@app.route('/testZoneInfoInstanceCaching', methods=['POST'])
def call_testZoneInfoInstanceCaching():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoInstanceCaching()

@app.route('/testZoneInfoNewInstance', methods=['POST'])
def call_testZoneInfoNewInstance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoNewInstance()

@app.route('/testZoneInfoDeprecated', methods=['POST'])
def call_testZoneInfoDeprecated():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoDeprecated()

@app.route('/testZoneInfoMetadataDeprecated', methods=['POST'])
def call_testZoneInfoMetadataDeprecated():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testZoneInfoMetadataDeprecated()

@app.route('/testRangeCmp1', methods=['POST'])
def call_testRangeCmp1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeCmp1()

@app.route('/testRangeCmp2', methods=['POST'])
def call_testRangeCmp2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeCmp2()

@app.route('/testRangeOffsets', methods=['POST'])
def call_testRangeOffsets():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeOffsets()

@app.route('/testTimeOnlyRangeFixed', methods=['POST'])
def call_testTimeOnlyRangeFixed():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyRangeFixed()

@app.route('/testTimeOnlyRange', methods=['POST'])
def call_testTimeOnlyRange():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTimeOnlyRange()

@app.route('/testBrokenIsDstHandling', methods=['POST'])
def call_testBrokenIsDstHandling():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBrokenIsDstHandling()

@app.route('/testRangeTimeDelta', methods=['POST'])
def call_testRangeTimeDelta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeTimeDelta()

@app.route('/testRangeEquality', methods=['POST'])
def call_testRangeEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeEquality()

@app.route('/testRangeInequalityUnsupported', methods=['POST'])
def call_testRangeInequalityUnsupported():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRangeInequalityUnsupported()

@app.route('/testStrStr', methods=['POST'])
def call_testStrStr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrStr()

@app.route('/testStrInequality', methods=['POST'])
def call_testStrInequality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrInequality()

@app.route('/testStrInequalityStartEnd', methods=['POST'])
def call_testStrInequalityStartEnd():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrInequalityStartEnd()

@app.route('/testPosixOffset', methods=['POST'])
def call_testPosixOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPosixOffset()

@app.route('/testStrInequalityUnsupported', methods=['POST'])
def call_testStrInequalityUnsupported():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrInequalityUnsupported()

@app.route('/testTzStrRepr', methods=['POST'])
def call_testTzStrRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzStrRepr()

@app.route('/testTzStrFailure', methods=['POST'])
def call_testTzStrFailure():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzStrFailure()

@app.route('/testTzStrSingleton', methods=['POST'])
def call_testTzStrSingleton():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzStrSingleton()

@app.route('/testTzStrSingletonPosix', methods=['POST'])
def call_testTzStrSingletonPosix():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzStrSingletonPosix()

@app.route('/testTzStrInstance', methods=['POST'])
def call_testTzStrInstance():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzStrInstance()

@app.route('/test_tzstr_weakref', methods=['POST'])
def call_test_tzstr_weakref():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzstr_weakref()

@app.route('/test_valid_GNU_tzstr', methods=['POST'])
def call_test_valid_GNU_tzstr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tz_str = request_json.get("tz_str")
    
    expected = request_json.get("expected")
    

    return test_valid_GNU_tzstr(tz_str, expected)

@app.route('/test_valid_dateutil_format', methods=['POST'])
def call_test_valid_dateutil_format():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tz_str = request_json.get("tz_str")
    
    expected = request_json.get("expected")
    

    return test_valid_dateutil_format(tz_str, expected)

@app.route('/test_invalid_GNU_tzstr', methods=['POST'])
def call_test_invalid_GNU_tzstr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tz_str = request_json.get("tz_str")
    

    return test_invalid_GNU_tzstr(tz_str)

@app.route('/test_tzstr_default_start', methods=['POST'])
def call_test_tzstr_default_start():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tz_str = request_json.get("tz_str")
    

    return test_tzstr_default_start(tz_str)

@app.route('/test_tzstr_default_end', methods=['POST'])
def call_test_tzstr_default_end():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tz_str = request_json.get("tz_str")
    

    return test_tzstr_default_end(tz_str)

@app.route('/test_tzstr_default_cmp', methods=['POST'])
def call_test_tzstr_default_cmp():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzstr_1 = request_json.get("tzstr_1")
    
    tzstr_2 = request_json.get("tzstr_2")
    

    return test_tzstr_default_cmp(tzstr_1, tzstr_2)

@app.route('/testESTStartName', methods=['POST'])
def call_testESTStartName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTStartName()

@app.route('/testESTEndName', methods=['POST'])
def call_testESTEndName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTEndName()

@app.route('/testESTStartOffset', methods=['POST'])
def call_testESTStartOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTStartOffset()

@app.route('/testESTEndOffset', methods=['POST'])
def call_testESTEndOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTEndOffset()

@app.route('/testESTStartDST', methods=['POST'])
def call_testESTStartDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTStartDST()

@app.route('/testESTEndDST', methods=['POST'])
def call_testESTEndDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTEndDST()

@app.route('/testESTValueDatetime', methods=['POST'])
def call_testESTValueDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testESTValueDatetime()

@app.route('/testMultiZoneStartName', methods=['POST'])
def call_testMultiZoneStartName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneStartName()

@app.route('/testMultiZoneEndName', methods=['POST'])
def call_testMultiZoneEndName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneEndName()

@app.route('/testMultiZoneStartOffset', methods=['POST'])
def call_testMultiZoneStartOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneStartOffset()

@app.route('/testMultiZoneEndOffset', methods=['POST'])
def call_testMultiZoneEndOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneEndOffset()

@app.route('/testMultiZoneStartDST', methods=['POST'])
def call_testMultiZoneStartDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneStartDST()

@app.route('/testMultiZoneEndDST', methods=['POST'])
def call_testMultiZoneEndDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneEndDST()

@app.route('/testMultiZoneKeys', methods=['POST'])
def call_testMultiZoneKeys():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneKeys()

@app.route('/testEmptyString', methods=['POST'])
def call_testEmptyString():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testEmptyString()

@app.route('/testMultiZoneGet', methods=['POST'])
def call_testMultiZoneGet():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMultiZoneGet()

@app.route('/testDtstartDate', methods=['POST'])
def call_testDtstartDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDtstartDate()

@app.route('/testDtstartTzid', methods=['POST'])
def call_testDtstartTzid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDtstartTzid()

@app.route('/testDtstartBadParam', methods=['POST'])
def call_testDtstartBadParam():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDtstartBadParam()

@app.route('/testGap', methods=['POST'])
def call_testGap():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGap()

@app.route('/testFileStart1', methods=['POST'])
def call_testFileStart1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFileStart1()

@app.route('/testFileEnd1', methods=['POST'])
def call_testFileEnd1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFileEnd1()

@app.route('/testFileLastTransition', methods=['POST'])
def call_testFileLastTransition():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFileLastTransition()

@app.route('/testInvalidFile', methods=['POST'])
def call_testInvalidFile():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInvalidFile()

@app.route('/testFilestreamWithNameRepr', methods=['POST'])
def call_testFilestreamWithNameRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFilestreamWithNameRepr()

@app.route('/testLeapCountDecodesProperly', methods=['POST'])
def call_testLeapCountDecodesProperly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLeapCountDecodesProperly()

@app.route('/testIsStd', methods=['POST'])
def call_testIsStd():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIsStd()

@app.route('/testGMTHasNoDaylight', methods=['POST'])
def call_testGMTHasNoDaylight():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGMTHasNoDaylight()

@app.route('/testGMTOffset', methods=['POST'])
def call_testGMTOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGMTOffset()

@app.route('/testTZSetDoesntCorrupt', methods=['POST'])
def call_testTZSetDoesntCorrupt():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTZSetDoesntCorrupt()

@app.route('/test_tzfile_sub_minute_offset', methods=['POST'])
def call_test_tzfile_sub_minute_offset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzfile_sub_minute_offset()

@app.route('/test_sub_minute_rounding_tzfile', methods=['POST'])
def call_test_sub_minute_rounding_tzfile():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_sub_minute_rounding_tzfile()

@app.route('/test_samoa_transition', methods=['POST'])
def call_test_samoa_transition():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_samoa_transition()

@app.route('/setUp', methods=['POST'])
def call_setUp():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return setUp()

@app.route('/testTzResLoadName', methods=['POST'])
def call_testTzResLoadName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzResLoadName()

@app.route('/testTzResNameFromString', methods=['POST'])
def call_testTzResNameFromString():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzResNameFromString()

@app.route('/testIsdstZoneWithNoDaylightSaving', methods=['POST'])
def call_testIsdstZoneWithNoDaylightSaving():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIsdstZoneWithNoDaylightSaving()

@app.route('/testTzwinName', methods=['POST'])
def call_testTzwinName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinName()

@app.route('/testTzwinRepr', methods=['POST'])
def call_testTzwinRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinRepr()

@app.route('/testTzWinEquality', methods=['POST'])
def call_testTzWinEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzWinEquality()

@app.route('/testTzWinInequality', methods=['POST'])
def call_testTzWinInequality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzWinInequality()

@app.route('/testTzWinEqualityInvalid', methods=['POST'])
def call_testTzWinEqualityInvalid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzWinEqualityInvalid()

@app.route('/testTzWinInequalityUnsupported', methods=['POST'])
def call_testTzWinInequalityUnsupported():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzWinInequalityUnsupported()

@app.route('/testTzwinTimeOnlyDST', methods=['POST'])
def call_testTzwinTimeOnlyDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinTimeOnlyDST()

@app.route('/testTzwinTimeOnlyUTCOffset', methods=['POST'])
def call_testTzwinTimeOnlyUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinTimeOnlyUTCOffset()

@app.route('/testTzwinTimeOnlyTZName', methods=['POST'])
def call_testTzwinTimeOnlyTZName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinTimeOnlyTZName()

@app.route('/testLocal', methods=['POST'])
def call_testLocal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLocal()

@app.route('/testTzwinLocalUTCOffset', methods=['POST'])
def call_testTzwinLocalUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalUTCOffset()

@app.route('/testTzwinLocalName', methods=['POST'])
def call_testTzwinLocalName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalName()

@app.route('/testTzWinLocalRepr', methods=['POST'])
def call_testTzWinLocalRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzWinLocalRepr()

@app.route('/testTzwinLocalRepr', methods=['POST'])
def call_testTzwinLocalRepr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalRepr()

@app.route('/testTzwinLocalEquality', methods=['POST'])
def call_testTzwinLocalEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalEquality()

@app.route('/testTzwinLocalTimeOnlyDST', methods=['POST'])
def call_testTzwinLocalTimeOnlyDST():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalTimeOnlyDST()

@app.route('/testTzwinLocalTimeOnlyUTCOffset', methods=['POST'])
def call_testTzwinLocalTimeOnlyUTCOffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalTimeOnlyUTCOffset()

@app.route('/testTzwinLocalTimeOnlyTZName', methods=['POST'])
def call_testTzwinLocalTimeOnlyTZName():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testTzwinLocalTimeOnlyTZName()

@app.route('/testPickleTzUTC', methods=['POST'])
def call_testPickleTzUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzUTC()

@app.route('/testPickleTzOffsetZero', methods=['POST'])
def call_testPickleTzOffsetZero():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzOffsetZero()

@app.route('/testPickleTzOffsetPos', methods=['POST'])
def call_testPickleTzOffsetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzOffsetPos()

@app.route('/testPickleTzOffsetNeg', methods=['POST'])
def call_testPickleTzOffsetNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzOffsetNeg()

@app.route('/testPickleTzLocal', methods=['POST'])
def call_testPickleTzLocal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzLocal()

@app.route('/testPickleTzFileEST5EDT', methods=['POST'])
def call_testPickleTzFileEST5EDT():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzFileEST5EDT()

@app.route('/testPickleTzFileEurope_Helsinki', methods=['POST'])
def call_testPickleTzFileEurope_Helsinki():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzFileEurope_Helsinki()

@app.route('/testPickleTzFileNew_York', methods=['POST'])
def call_testPickleTzFileNew_York():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzFileNew_York()

@app.route('/testPickleTzICal', methods=['POST'])
def call_testPickleTzICal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzICal()

@app.route('/testPickleTzGettz', methods=['POST'])
def call_testPickleTzGettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleTzGettz()

@app.route('/testPickleZoneFileGettz', methods=['POST'])
def call_testPickleZoneFileGettz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPickleZoneFileGettz()

@app.route('/testNoTzSpecified', methods=['POST'])
def call_testNoTzSpecified():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoTzSpecified()

@app.route('/testNoSupportAmbiguityFoldNaive', methods=['POST'])
def call_testNoSupportAmbiguityFoldNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityFoldNaive()

@app.route('/testNoSupportAmbiguityFoldAware', methods=['POST'])
def call_testNoSupportAmbiguityFoldAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityFoldAware()

@app.route('/testNoSupportAmbiguityUnambiguousNaive', methods=['POST'])
def call_testNoSupportAmbiguityUnambiguousNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityUnambiguousNaive()

@app.route('/testNoSupportAmbiguityUnambiguousAware', methods=['POST'])
def call_testNoSupportAmbiguityUnambiguousAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityUnambiguousAware()

@app.route('/testNoSupportAmbiguityFoldDSTOnly', methods=['POST'])
def call_testNoSupportAmbiguityFoldDSTOnly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityFoldDSTOnly()

@app.route('/testNoSupportAmbiguityUnambiguousDSTOnly', methods=['POST'])
def call_testNoSupportAmbiguityUnambiguousDSTOnly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoSupportAmbiguityUnambiguousDSTOnly()

@app.route('/testSupportAmbiguityFoldNaive', methods=['POST'])
def call_testSupportAmbiguityFoldNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSupportAmbiguityFoldNaive()

@app.route('/testSupportAmbiguityFoldAware', methods=['POST'])
def call_testSupportAmbiguityFoldAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSupportAmbiguityFoldAware()

@app.route('/testSupportAmbiguityUnambiguousAware', methods=['POST'])
def call_testSupportAmbiguityUnambiguousAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSupportAmbiguityUnambiguousAware()

@app.route('/testSupportAmbiguityUnambiguousNaive', methods=['POST'])
def call_testSupportAmbiguityUnambiguousNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSupportAmbiguityUnambiguousNaive()

@app.route('/testIncompatibleAmbiguityFoldNaive', methods=['POST'])
def call_testIncompatibleAmbiguityFoldNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityFoldNaive()

@app.route('/testIncompatibleAmbiguityFoldAware', methods=['POST'])
def call_testIncompatibleAmbiguityFoldAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityFoldAware()

@app.route('/testIncompatibleAmbiguityUnambiguousNaive', methods=['POST'])
def call_testIncompatibleAmbiguityUnambiguousNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityUnambiguousNaive()

@app.route('/testIncompatibleAmbiguityUnambiguousAware', methods=['POST'])
def call_testIncompatibleAmbiguityUnambiguousAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityUnambiguousAware()

@app.route('/testIncompatibleAmbiguityFoldDSTOnly', methods=['POST'])
def call_testIncompatibleAmbiguityFoldDSTOnly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityFoldDSTOnly()

@app.route('/testIncompatibleAmbiguityUnambiguousDSTOnly', methods=['POST'])
def call_testIncompatibleAmbiguityUnambiguousDSTOnly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncompatibleAmbiguityUnambiguousDSTOnly()

@app.route('/testSpecifiedTzOverridesAttached', methods=['POST'])
def call_testSpecifiedTzOverridesAttached():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSpecifiedTzOverridesAttached()

@app.route('/testInGapNaive', methods=['POST'])
def call_testInGapNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInGapNaive()

@app.route('/testInGapAware', methods=['POST'])
def call_testInGapAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInGapAware()

@app.route('/testExistsNaive', methods=['POST'])
def call_testExistsNaive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testExistsNaive()

@app.route('/testExistsAware', methods=['POST'])
def call_testExistsAware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testExistsAware()

@app.route('/test_enter_fold_default', methods=['POST'])
def call_test_enter_fold_default():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_enter_fold_default()

@app.route('/test_enter_fold', methods=['POST'])
def call_test_enter_fold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_enter_fold()

@app.route('/test_exit_fold', methods=['POST'])
def call_test_exit_fold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_exit_fold()

@app.route('/test_defold', methods=['POST'])
def call_test_defold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_defold()

@app.route('/test_fold_replace_args', methods=['POST'])
def call_test_fold_replace_args():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_fold_replace_args()

@app.route('/test_fold_replace_exception_duplicate_args', methods=['POST'])
def call_test_fold_replace_exception_duplicate_args():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_fold_replace_exception_duplicate_args()

@app.route('/testCanberraForward', methods=['POST'])
def call_testCanberraForward():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCanberraForward()

@app.route('/testLondonForward', methods=['POST'])
def call_testLondonForward():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLondonForward()

@app.route('/testKeivForward', methods=['POST'])
def call_testKeivForward():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testKeivForward()

@app.route('/test_resolve_imaginary_ambiguous', methods=['POST'])
def call_test_resolve_imaginary_ambiguous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return test_resolve_imaginary_ambiguous(dt)

@app.route('/test_resolve_imaginary_existing', methods=['POST'])
def call_test_resolve_imaginary_existing():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return test_resolve_imaginary_existing(dt)

@app.route('/test_resolve_imaginary', methods=['POST'])
def call_test_resolve_imaginary():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzi = request_json.get("tzi")
    
    dt = request_json.get("dt")
    
    dt_exp = request_json.get("dt_exp")
    

    return test_resolve_imaginary(tzi, dt, dt_exp)

@app.route('/test_utils_today', methods=['POST'])
def call_test_utils_today():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_today()

@app.route('/test_utils_today_tz_info', methods=['POST'])
def call_test_utils_today_tz_info():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_today_tz_info()

@app.route('/test_utils_today_tz_info_different_day', methods=['POST'])
def call_test_utils_today_tz_info_different_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_today_tz_info_different_day()

@app.route('/test_utils_default_tz_info_naive', methods=['POST'])
def call_test_utils_default_tz_info_naive():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_default_tz_info_naive()

@app.route('/test_utils_default_tz_info_aware', methods=['POST'])
def call_test_utils_default_tz_info_aware():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_default_tz_info_aware()

@app.route('/test_utils_within_delta', methods=['POST'])
def call_test_utils_within_delta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_within_delta()

@app.route('/test_utils_within_delta_with_negative_delta', methods=['POST'])
def call_test_utils_within_delta_with_negative_delta():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_utils_within_delta_with_negative_delta()

@app.route('/assertPicklable', methods=['POST'])
def call_assertPicklable():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    obj = request_json.get("obj")
    
    singleton = request_json.get("singleton")
    
    asfile = request_json.get("asfile")
    
    dump_kwargs = request_json.get("dump_kwargs")
    
    load_kwargs = request_json.get("load_kwargs")
    

    return assertPicklable(obj, singleton, asfile, dump_kwargs, load_kwargs)

@app.route('/tz_change_allowed', methods=['POST'])
def call_tz_change_allowed():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    

    return tz_change_allowed(cls)

@app.route('/tz_change_disallowed_message', methods=['POST'])
def call_tz_change_disallowed_message():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    

    return tz_change_disallowed_message(cls)

@app.route('/get_current_tz', methods=['POST'])
def call_get_current_tz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return get_current_tz()

@app.route('/set_current_tz', methods=['POST'])
def call_set_current_tz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzname = request_json.get("tzname")
    

    return set_current_tz(tzname)

@app.route('/fuzzy', methods=['POST'])
def call_fuzzy():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    request = request_json.get("request")
    

    return fuzzy(request)

@app.route('/test_parser', methods=['POST'])
def call_test_parser():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    parsable_text = request_json.get("parsable_text")
    
    expected_datetime = request_json.get("expected_datetime")
    
    assertion_message = request_json.get("assertion_message")
    

    return test_parser(parsable_text, expected_datetime, assertion_message)

@app.route('/test_parser_default', methods=['POST'])
def call_test_parser_default():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    parsable_text = request_json.get("parsable_text")
    
    expected_datetime = request_json.get("expected_datetime")
    
    assertion_message = request_json.get("assertion_message")
    

    return test_parser_default(parsable_text, expected_datetime, assertion_message)

@app.route('/test_parse_dayfirst', methods=['POST'])
def call_test_parse_dayfirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    sep = request_json.get("sep")
    

    return test_parse_dayfirst(sep)

@app.route('/test_parse_yearfirst', methods=['POST'])
def call_test_parse_yearfirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    sep = request_json.get("sep")
    

    return test_parse_yearfirst(sep)

@app.route('/test_parse_ignoretz', methods=['POST'])
def call_test_parse_ignoretz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dstr = request_json.get("dstr")
    
    expected = request_json.get("expected")
    

    return test_parse_ignoretz(dstr, expected)

@app.route('/test_parse_with_tzoffset', methods=['POST'])
def call_test_parse_with_tzoffset():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dstr = request_json.get("dstr")
    
    expected = request_json.get("expected")
    

    return test_parse_with_tzoffset(dstr, expected)

@app.route('/test_ybd', methods=['POST'])
def call_test_ybd():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_ybd()

@app.route('/test_strftime_formats_2003Sep25', methods=['POST'])
def call_test_strftime_formats_2003Sep25():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fmt = request_json.get("fmt")
    
    dstr = request_json.get("dstr")
    

    return test_strftime_formats_2003Sep25(fmt, dstr)

@app.route('/test_empty_string_invalid', methods=['POST'])
def call_test_empty_string_invalid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_empty_string_invalid()

@app.route('/test_none_invalid', methods=['POST'])
def call_test_none_invalid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_none_invalid()

@app.route('/test_int_invalid', methods=['POST'])
def call_test_int_invalid():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_int_invalid()

@app.route('/test_duck_typing', methods=['POST'])
def call_test_duck_typing():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_duck_typing()

@app.route('/test_parse_stream', methods=['POST'])
def call_test_parse_stream():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_stream()

@app.route('/test_parse_str', methods=['POST'])
def call_test_parse_str():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_str()

@app.route('/test_parse_bytes', methods=['POST'])
def call_test_parse_bytes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_bytes()

@app.route('/test_parse_bytearray', methods=['POST'])
def call_test_parse_bytearray():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_bytearray()

@app.route('/assert_equal_same_tz', methods=['POST'])
def call_assert_equal_same_tz():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt1 = request_json.get("dt1")
    
    dt2 = request_json.get("dt2")
    

    return assert_equal_same_tz(dt1, dt2)

@app.route('/test_tzinfo_dict_could_return_none', methods=['POST'])
def call_test_tzinfo_dict_could_return_none():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzinfo_dict_could_return_none()

@app.route('/test_tzinfos_callable_could_return_none', methods=['POST'])
def call_test_tzinfos_callable_could_return_none():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzinfos_callable_could_return_none()

@app.route('/test_invalid_tzinfo_input', methods=['POST'])
def call_test_invalid_tzinfo_input():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_invalid_tzinfo_input()

@app.route('/test_valid_tzinfo_tzinfo_input', methods=['POST'])
def call_test_valid_tzinfo_tzinfo_input():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_valid_tzinfo_tzinfo_input()

@app.route('/test_valid_tzinfo_unicode_input', methods=['POST'])
def call_test_valid_tzinfo_unicode_input():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_valid_tzinfo_unicode_input()

@app.route('/test_valid_tzinfo_callable_input', methods=['POST'])
def call_test_valid_tzinfo_callable_input():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_valid_tzinfo_callable_input()

@app.route('/test_valid_tzinfo_int_input', methods=['POST'])
def call_test_valid_tzinfo_int_input():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_valid_tzinfo_int_input()

@app.route('/setup_class', methods=['POST'])
def call_setup_class():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cls = request_json.get("cls")
    

    return setup_class(cls)

@app.route('/testParserParseStr', methods=['POST'])
def call_testParserParseStr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testParserParseStr()

@app.route('/testParseUnicodeWords', methods=['POST'])
def call_testParseUnicodeWords():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testParseUnicodeWords()

@app.route('/testParseWithNulls', methods=['POST'])
def call_testParseWithNulls():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testParseWithNulls()

@app.route('/testDateCommandFormat', methods=['POST'])
def call_testDateCommandFormat():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDateCommandFormat()

@app.route('/testDateCommandFormatReversed', methods=['POST'])
def call_testDateCommandFormatReversed():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDateCommandFormatReversed()

@app.route('/testDateCommandFormatWithLong', methods=['POST'])
def call_testDateCommandFormatWithLong():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDateCommandFormatWithLong()

@app.route('/testISOFormatStrip2', methods=['POST'])
def call_testISOFormatStrip2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testISOFormatStrip2()

@app.route('/testISOStrippedFormatStrip2', methods=['POST'])
def call_testISOStrippedFormatStrip2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testISOStrippedFormatStrip2()

@app.route('/testAMPMNoHour', methods=['POST'])
def call_testAMPMNoHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAMPMNoHour()

@app.route('/testAMPMRange', methods=['POST'])
def call_testAMPMRange():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAMPMRange()

@app.route('/testPertain', methods=['POST'])
def call_testPertain():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testPertain()

@app.route('/testFuzzy', methods=['POST'])
def call_testFuzzy():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFuzzy()

@app.route('/testFuzzyWithTokens', methods=['POST'])
def call_testFuzzyWithTokens():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFuzzyWithTokens()

@app.route('/testFuzzyAMPMProblem', methods=['POST'])
def call_testFuzzyAMPMProblem():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFuzzyAMPMProblem()

@app.route('/testFuzzyIgnoreAMPM', methods=['POST'])
def call_testFuzzyIgnoreAMPM():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testFuzzyIgnoreAMPM()

@app.route('/testRandomFormat24', methods=['POST'])
def call_testRandomFormat24():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRandomFormat24()

@app.route('/testRandomFormat26', methods=['POST'])
def call_testRandomFormat26():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testRandomFormat26()

@app.route('/testUnspecifiedDayFallback', methods=['POST'])
def call_testUnspecifiedDayFallback():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnspecifiedDayFallback()

@app.route('/testUnspecifiedDayFallbackFebNoLeapYear', methods=['POST'])
def call_testUnspecifiedDayFallbackFebNoLeapYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnspecifiedDayFallbackFebNoLeapYear()

@app.route('/testUnspecifiedDayFallbackFebLeapYear', methods=['POST'])
def call_testUnspecifiedDayFallbackFebLeapYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnspecifiedDayFallbackFebLeapYear()

@app.route('/testErrorType01', methods=['POST'])
def call_testErrorType01():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testErrorType01()

@app.route('/testCorrectErrorOnFuzzyWithTokens', methods=['POST'])
def call_testCorrectErrorOnFuzzyWithTokens():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCorrectErrorOnFuzzyWithTokens()

@app.route('/testIncreasingCTime', methods=['POST'])
def call_testIncreasingCTime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncreasingCTime()

@app.route('/testIncreasingISOFormat', methods=['POST'])
def call_testIncreasingISOFormat():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testIncreasingISOFormat()

@app.route('/testMicrosecondsPrecisionError', methods=['POST'])
def call_testMicrosecondsPrecisionError():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMicrosecondsPrecisionError()

@app.route('/testMicrosecondPrecisionErrorReturns', methods=['POST'])
def call_testMicrosecondPrecisionErrorReturns():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMicrosecondPrecisionErrorReturns()

@app.route('/testCustomParserInfo', methods=['POST'])
def call_testCustomParserInfo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCustomParserInfo()

@app.route('/testCustomParserShortDaynames', methods=['POST'])
def call_testCustomParserShortDaynames():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCustomParserShortDaynames()

@app.route('/testNoYearFirstNoDayFirst', methods=['POST'])
def call_testNoYearFirstNoDayFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testNoYearFirstNoDayFirst()

@app.route('/testYearFirst', methods=['POST'])
def call_testYearFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearFirst()

@app.route('/testDayFirst', methods=['POST'])
def call_testDayFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDayFirst()

@app.route('/testDayFirstYearFirst', methods=['POST'])
def call_testDayFirstYearFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDayFirstYearFirst()

@app.route('/testUnambiguousYearFirst', methods=['POST'])
def call_testUnambiguousYearFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousYearFirst()

@app.route('/testUnambiguousDayFirst', methods=['POST'])
def call_testUnambiguousDayFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousDayFirst()

@app.route('/testUnambiguousDayFirstYearFirst', methods=['POST'])
def call_testUnambiguousDayFirstYearFirst():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUnambiguousDayFirstYearFirst()

@app.route('/test_mstridx', methods=['POST'])
def call_test_mstridx():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_mstridx()

@app.route('/test_idx_check', methods=['POST'])
def call_test_idx_check():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_idx_check()

@app.route('/test_hmBY', methods=['POST'])
def call_test_hmBY():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_hmBY()

@app.route('/test_validate_hour', methods=['POST'])
def call_test_validate_hour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_validate_hour()

@app.route('/test_era_trailing_year', methods=['POST'])
def call_test_era_trailing_year():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_era_trailing_year()

@app.route('/test_includes_timestr', methods=['POST'])
def call_test_includes_timestr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_includes_timestr()

@app.route('/test_no_year_zero', methods=['POST'])
def call_test_no_year_zero():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_no_year_zero()

@app.route('/test_out_of_bound_day', methods=['POST'])
def call_test_out_of_bound_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_out_of_bound_day()

@app.route('/test_illegal_month_error', methods=['POST'])
def call_test_illegal_month_error():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_illegal_month_error()

@app.route('/test_day_sanity', methods=['POST'])
def call_test_day_sanity():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fuzzy = request_json.get("fuzzy")
    

    return test_day_sanity(fuzzy)

@app.route('/test_minute_sanity', methods=['POST'])
def call_test_minute_sanity():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fuzzy = request_json.get("fuzzy")
    

    return test_minute_sanity(fuzzy)

@app.route('/test_hour_sanity', methods=['POST'])
def call_test_hour_sanity():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fuzzy = request_json.get("fuzzy")
    

    return test_hour_sanity(fuzzy)

@app.route('/test_second_sanity', methods=['POST'])
def call_test_second_sanity():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fuzzy = request_json.get("fuzzy")
    

    return test_second_sanity(fuzzy)

@app.route('/test_somewhat_ambiguous_string', methods=['POST'])
def call_test_somewhat_ambiguous_string():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_somewhat_ambiguous_string()

@app.route('/test_YmdH_M_S', methods=['POST'])
def call_test_YmdH_M_S():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_YmdH_M_S()

@app.route('/test_first_century', methods=['POST'])
def call_test_first_century():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_first_century()

@app.route('/test_era_trailing_year_with_dots', methods=['POST'])
def call_test_era_trailing_year_with_dots():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_era_trailing_year_with_dots()

@app.route('/test_ad_nospace', methods=['POST'])
def call_test_ad_nospace():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_ad_nospace()

@app.route('/test_four_letter_day', methods=['POST'])
def call_test_four_letter_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_four_letter_day()

@app.route('/test_non_date_number', methods=['POST'])
def call_test_non_date_number():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_non_date_number()

@app.route('/test_on_era', methods=['POST'])
def call_test_on_era():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_on_era()

@app.route('/test_extraneous_year', methods=['POST'])
def call_test_extraneous_year():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_extraneous_year()

@app.route('/test_extraneous_year_tokens', methods=['POST'])
def call_test_extraneous_year_tokens():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_extraneous_year_tokens()

@app.route('/test_extraneous_year2', methods=['POST'])
def call_test_extraneous_year2():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_extraneous_year2()

@app.route('/test_extraneous_year3', methods=['POST'])
def call_test_extraneous_year3():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_extraneous_year3()

@app.route('/test_unambiguous_YYYYMM', methods=['POST'])
def call_test_unambiguous_YYYYMM():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_unambiguous_YYYYMM()

@app.route('/test_extraneous_numerical_content', methods=['POST'])
def call_test_extraneous_numerical_content():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_extraneous_numerical_content()

@app.route('/test_parse_unambiguous_nonexistent_local', methods=['POST'])
def call_test_parse_unambiguous_nonexistent_local():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_unambiguous_nonexistent_local()

@app.route('/test_tzlocal_in_gmt', methods=['POST'])
def call_test_tzlocal_in_gmt():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzlocal_in_gmt()

@app.route('/test_tzlocal_parse_fold', methods=['POST'])
def call_test_tzlocal_parse_fold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzlocal_parse_fold()

@app.route('/test_parse_tzinfos_fold', methods=['POST'])
def call_test_parse_tzinfos_fold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_tzinfos_fold()

@app.route('/test_rounding_floatlike_strings', methods=['POST'])
def call_test_rounding_floatlike_strings():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dtstr = request_json.get("dtstr")
    
    dt = request_json.get("dt")
    

    return test_rounding_floatlike_strings(dtstr, dt)

@app.route('/test_decimal_error', methods=['POST'])
def call_test_decimal_error():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    value = request_json.get("value")
    

    return test_decimal_error(value)

@app.route('/test_parsererror_repr', methods=['POST'])
def call_test_parsererror_repr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parsererror_repr()

@app.route('/testStrAppendRRULEToken', methods=['POST'])
def call_testStrAppendRRULEToken():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrAppendRRULEToken()

@app.route('/testYearly', methods=['POST'])
def call_testYearly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearly()

@app.route('/testYearlyInterval', methods=['POST'])
def call_testYearlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyInterval()

@app.route('/testYearlyIntervalLarge', methods=['POST'])
def call_testYearlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyIntervalLarge()

@app.route('/testYearlyByMonth', methods=['POST'])
def call_testYearlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonth()

@app.route('/testYearlyByMonthDay', methods=['POST'])
def call_testYearlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthDay()

@app.route('/testYearlyByMonthAndMonthDay', methods=['POST'])
def call_testYearlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndMonthDay()

@app.route('/testYearlyByWeekDay', methods=['POST'])
def call_testYearlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekDay()

@app.route('/testYearlyByNWeekDay', methods=['POST'])
def call_testYearlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByNWeekDay()

@app.route('/testYearlyByNWeekDayLarge', methods=['POST'])
def call_testYearlyByNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByNWeekDayLarge()

@app.route('/testYearlyByMonthAndWeekDay', methods=['POST'])
def call_testYearlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndWeekDay()

@app.route('/testYearlyByMonthAndNWeekDay', methods=['POST'])
def call_testYearlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndNWeekDay()

@app.route('/testYearlyByMonthAndNWeekDayLarge', methods=['POST'])
def call_testYearlyByMonthAndNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndNWeekDayLarge()

@app.route('/testYearlyByMonthDayAndWeekDay', methods=['POST'])
def call_testYearlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthDayAndWeekDay()

@app.route('/testYearlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testYearlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndMonthDayAndWeekDay()

@app.route('/testYearlyByYearDay', methods=['POST'])
def call_testYearlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByYearDay()

@app.route('/testYearlyByYearDayNeg', methods=['POST'])
def call_testYearlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByYearDayNeg()

@app.route('/testYearlyByMonthAndYearDay', methods=['POST'])
def call_testYearlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndYearDay()

@app.route('/testYearlyByMonthAndYearDayNeg', methods=['POST'])
def call_testYearlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMonthAndYearDayNeg()

@app.route('/testYearlyByWeekNo', methods=['POST'])
def call_testYearlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekNo()

@app.route('/testYearlyByWeekNoAndWeekDay', methods=['POST'])
def call_testYearlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekNoAndWeekDay()

@app.route('/testYearlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testYearlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekNoAndWeekDayLarge()

@app.route('/testYearlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testYearlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekNoAndWeekDayLast()

@app.route('/testYearlyByEaster', methods=['POST'])
def call_testYearlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByEaster()

@app.route('/testYearlyByEasterPos', methods=['POST'])
def call_testYearlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByEasterPos()

@app.route('/testYearlyByEasterNeg', methods=['POST'])
def call_testYearlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByEasterNeg()

@app.route('/testYearlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testYearlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByWeekNoAndWeekDay53()

@app.route('/testYearlyByHour', methods=['POST'])
def call_testYearlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByHour()

@app.route('/testYearlyByMinute', methods=['POST'])
def call_testYearlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMinute()

@app.route('/testYearlyBySecond', methods=['POST'])
def call_testYearlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyBySecond()

@app.route('/testYearlyByHourAndMinute', methods=['POST'])
def call_testYearlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByHourAndMinute()

@app.route('/testYearlyByHourAndSecond', methods=['POST'])
def call_testYearlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByHourAndSecond()

@app.route('/testYearlyByMinuteAndSecond', methods=['POST'])
def call_testYearlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByMinuteAndSecond()

@app.route('/testYearlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testYearlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyByHourAndMinuteAndSecond()

@app.route('/testYearlyBySetPos', methods=['POST'])
def call_testYearlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testYearlyBySetPos()

@app.route('/testMonthly', methods=['POST'])
def call_testMonthly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthly()

@app.route('/testMonthlyInterval', methods=['POST'])
def call_testMonthlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyInterval()

@app.route('/testMonthlyIntervalLarge', methods=['POST'])
def call_testMonthlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyIntervalLarge()

@app.route('/testMonthlyByMonth', methods=['POST'])
def call_testMonthlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonth()

@app.route('/testMonthlyByMonthDay', methods=['POST'])
def call_testMonthlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthDay()

@app.route('/testMonthlyByMonthAndMonthDay', methods=['POST'])
def call_testMonthlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndMonthDay()

@app.route('/testMonthlyByWeekDay', methods=['POST'])
def call_testMonthlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekDay()

@app.route('/testMonthlyByNWeekDay', methods=['POST'])
def call_testMonthlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByNWeekDay()

@app.route('/testMonthlyByNWeekDayLarge', methods=['POST'])
def call_testMonthlyByNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByNWeekDayLarge()

@app.route('/testMonthlyByMonthAndWeekDay', methods=['POST'])
def call_testMonthlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndWeekDay()

@app.route('/testMonthlyByMonthAndNWeekDay', methods=['POST'])
def call_testMonthlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndNWeekDay()

@app.route('/testMonthlyByMonthAndNWeekDayLarge', methods=['POST'])
def call_testMonthlyByMonthAndNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndNWeekDayLarge()

@app.route('/testMonthlyByMonthDayAndWeekDay', methods=['POST'])
def call_testMonthlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthDayAndWeekDay()

@app.route('/testMonthlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testMonthlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndMonthDayAndWeekDay()

@app.route('/testMonthlyByYearDay', methods=['POST'])
def call_testMonthlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByYearDay()

@app.route('/testMonthlyByYearDayNeg', methods=['POST'])
def call_testMonthlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByYearDayNeg()

@app.route('/testMonthlyByMonthAndYearDay', methods=['POST'])
def call_testMonthlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndYearDay()

@app.route('/testMonthlyByMonthAndYearDayNeg', methods=['POST'])
def call_testMonthlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMonthAndYearDayNeg()

@app.route('/testMonthlyByWeekNo', methods=['POST'])
def call_testMonthlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekNo()

@app.route('/testMonthlyByWeekNoAndWeekDay', methods=['POST'])
def call_testMonthlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekNoAndWeekDay()

@app.route('/testMonthlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testMonthlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekNoAndWeekDayLarge()

@app.route('/testMonthlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testMonthlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekNoAndWeekDayLast()

@app.route('/testMonthlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testMonthlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByWeekNoAndWeekDay53()

@app.route('/testMonthlyByEaster', methods=['POST'])
def call_testMonthlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByEaster()

@app.route('/testMonthlyByEasterPos', methods=['POST'])
def call_testMonthlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByEasterPos()

@app.route('/testMonthlyByEasterNeg', methods=['POST'])
def call_testMonthlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByEasterNeg()

@app.route('/testMonthlyByHour', methods=['POST'])
def call_testMonthlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByHour()

@app.route('/testMonthlyByMinute', methods=['POST'])
def call_testMonthlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMinute()

@app.route('/testMonthlyBySecond', methods=['POST'])
def call_testMonthlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyBySecond()

@app.route('/testMonthlyByHourAndMinute', methods=['POST'])
def call_testMonthlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByHourAndMinute()

@app.route('/testMonthlyByHourAndSecond', methods=['POST'])
def call_testMonthlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByHourAndSecond()

@app.route('/testMonthlyByMinuteAndSecond', methods=['POST'])
def call_testMonthlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByMinuteAndSecond()

@app.route('/testMonthlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testMonthlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyByHourAndMinuteAndSecond()

@app.route('/testMonthlyBySetPos', methods=['POST'])
def call_testMonthlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMonthlyBySetPos()

@app.route('/testWeekly', methods=['POST'])
def call_testWeekly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekly()

@app.route('/testWeeklyInterval', methods=['POST'])
def call_testWeeklyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyInterval()

@app.route('/testWeeklyIntervalLarge', methods=['POST'])
def call_testWeeklyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyIntervalLarge()

@app.route('/testWeeklyByMonth', methods=['POST'])
def call_testWeeklyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonth()

@app.route('/testWeeklyByMonthDay', methods=['POST'])
def call_testWeeklyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthDay()

@app.route('/testWeeklyByMonthAndMonthDay', methods=['POST'])
def call_testWeeklyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndMonthDay()

@app.route('/testWeeklyByWeekDay', methods=['POST'])
def call_testWeeklyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekDay()

@app.route('/testWeeklyByNWeekDay', methods=['POST'])
def call_testWeeklyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByNWeekDay()

@app.route('/testWeeklyByMonthAndWeekDay', methods=['POST'])
def call_testWeeklyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndWeekDay()

@app.route('/testWeeklyByMonthAndNWeekDay', methods=['POST'])
def call_testWeeklyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndNWeekDay()

@app.route('/testWeeklyByMonthDayAndWeekDay', methods=['POST'])
def call_testWeeklyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthDayAndWeekDay()

@app.route('/testWeeklyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testWeeklyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndMonthDayAndWeekDay()

@app.route('/testWeeklyByYearDay', methods=['POST'])
def call_testWeeklyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByYearDay()

@app.route('/testWeeklyByYearDayNeg', methods=['POST'])
def call_testWeeklyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByYearDayNeg()

@app.route('/testWeeklyByMonthAndYearDay', methods=['POST'])
def call_testWeeklyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndYearDay()

@app.route('/testWeeklyByMonthAndYearDayNeg', methods=['POST'])
def call_testWeeklyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMonthAndYearDayNeg()

@app.route('/testWeeklyByWeekNo', methods=['POST'])
def call_testWeeklyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekNo()

@app.route('/testWeeklyByWeekNoAndWeekDay', methods=['POST'])
def call_testWeeklyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekNoAndWeekDay()

@app.route('/testWeeklyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testWeeklyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekNoAndWeekDayLarge()

@app.route('/testWeeklyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testWeeklyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekNoAndWeekDayLast()

@app.route('/testWeeklyByWeekNoAndWeekDay53', methods=['POST'])
def call_testWeeklyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByWeekNoAndWeekDay53()

@app.route('/testWeeklyByEaster', methods=['POST'])
def call_testWeeklyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByEaster()

@app.route('/testWeeklyByEasterPos', methods=['POST'])
def call_testWeeklyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByEasterPos()

@app.route('/testWeeklyByEasterNeg', methods=['POST'])
def call_testWeeklyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByEasterNeg()

@app.route('/testWeeklyByHour', methods=['POST'])
def call_testWeeklyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByHour()

@app.route('/testWeeklyByMinute', methods=['POST'])
def call_testWeeklyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMinute()

@app.route('/testWeeklyBySecond', methods=['POST'])
def call_testWeeklyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyBySecond()

@app.route('/testWeeklyByHourAndMinute', methods=['POST'])
def call_testWeeklyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByHourAndMinute()

@app.route('/testWeeklyByHourAndSecond', methods=['POST'])
def call_testWeeklyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByHourAndSecond()

@app.route('/testWeeklyByMinuteAndSecond', methods=['POST'])
def call_testWeeklyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByMinuteAndSecond()

@app.route('/testWeeklyByHourAndMinuteAndSecond', methods=['POST'])
def call_testWeeklyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyByHourAndMinuteAndSecond()

@app.route('/testWeeklyBySetPos', methods=['POST'])
def call_testWeeklyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeeklyBySetPos()

@app.route('/testDaily', methods=['POST'])
def call_testDaily():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDaily()

@app.route('/testDailyInterval', methods=['POST'])
def call_testDailyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyInterval()

@app.route('/testDailyIntervalLarge', methods=['POST'])
def call_testDailyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyIntervalLarge()

@app.route('/testDailyByMonth', methods=['POST'])
def call_testDailyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonth()

@app.route('/testDailyByMonthDay', methods=['POST'])
def call_testDailyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthDay()

@app.route('/testDailyByMonthAndMonthDay', methods=['POST'])
def call_testDailyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndMonthDay()

@app.route('/testDailyByWeekDay', methods=['POST'])
def call_testDailyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekDay()

@app.route('/testDailyByNWeekDay', methods=['POST'])
def call_testDailyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByNWeekDay()

@app.route('/testDailyByMonthAndWeekDay', methods=['POST'])
def call_testDailyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndWeekDay()

@app.route('/testDailyByMonthAndNWeekDay', methods=['POST'])
def call_testDailyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndNWeekDay()

@app.route('/testDailyByMonthDayAndWeekDay', methods=['POST'])
def call_testDailyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthDayAndWeekDay()

@app.route('/testDailyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testDailyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndMonthDayAndWeekDay()

@app.route('/testDailyByYearDay', methods=['POST'])
def call_testDailyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByYearDay()

@app.route('/testDailyByYearDayNeg', methods=['POST'])
def call_testDailyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByYearDayNeg()

@app.route('/testDailyByMonthAndYearDay', methods=['POST'])
def call_testDailyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndYearDay()

@app.route('/testDailyByMonthAndYearDayNeg', methods=['POST'])
def call_testDailyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMonthAndYearDayNeg()

@app.route('/testDailyByWeekNo', methods=['POST'])
def call_testDailyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekNo()

@app.route('/testDailyByWeekNoAndWeekDay', methods=['POST'])
def call_testDailyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekNoAndWeekDay()

@app.route('/testDailyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testDailyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekNoAndWeekDayLarge()

@app.route('/testDailyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testDailyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekNoAndWeekDayLast()

@app.route('/testDailyByWeekNoAndWeekDay53', methods=['POST'])
def call_testDailyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByWeekNoAndWeekDay53()

@app.route('/testDailyByEaster', methods=['POST'])
def call_testDailyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByEaster()

@app.route('/testDailyByEasterPos', methods=['POST'])
def call_testDailyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByEasterPos()

@app.route('/testDailyByEasterNeg', methods=['POST'])
def call_testDailyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByEasterNeg()

@app.route('/testDailyByHour', methods=['POST'])
def call_testDailyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByHour()

@app.route('/testDailyByMinute', methods=['POST'])
def call_testDailyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMinute()

@app.route('/testDailyBySecond', methods=['POST'])
def call_testDailyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyBySecond()

@app.route('/testDailyByHourAndMinute', methods=['POST'])
def call_testDailyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByHourAndMinute()

@app.route('/testDailyByHourAndSecond', methods=['POST'])
def call_testDailyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByHourAndSecond()

@app.route('/testDailyByMinuteAndSecond', methods=['POST'])
def call_testDailyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByMinuteAndSecond()

@app.route('/testDailyByHourAndMinuteAndSecond', methods=['POST'])
def call_testDailyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyByHourAndMinuteAndSecond()

@app.route('/testDailyBySetPos', methods=['POST'])
def call_testDailyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDailyBySetPos()

@app.route('/testHourly', methods=['POST'])
def call_testHourly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourly()

@app.route('/testHourlyInterval', methods=['POST'])
def call_testHourlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyInterval()

@app.route('/testHourlyIntervalLarge', methods=['POST'])
def call_testHourlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyIntervalLarge()

@app.route('/testHourlyByMonth', methods=['POST'])
def call_testHourlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonth()

@app.route('/testHourlyByMonthDay', methods=['POST'])
def call_testHourlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthDay()

@app.route('/testHourlyByMonthAndMonthDay', methods=['POST'])
def call_testHourlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndMonthDay()

@app.route('/testHourlyByWeekDay', methods=['POST'])
def call_testHourlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekDay()

@app.route('/testHourlyByNWeekDay', methods=['POST'])
def call_testHourlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByNWeekDay()

@app.route('/testHourlyByMonthAndWeekDay', methods=['POST'])
def call_testHourlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndWeekDay()

@app.route('/testHourlyByMonthAndNWeekDay', methods=['POST'])
def call_testHourlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndNWeekDay()

@app.route('/testHourlyByMonthDayAndWeekDay', methods=['POST'])
def call_testHourlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthDayAndWeekDay()

@app.route('/testHourlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testHourlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndMonthDayAndWeekDay()

@app.route('/testHourlyByYearDay', methods=['POST'])
def call_testHourlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByYearDay()

@app.route('/testHourlyByYearDayNeg', methods=['POST'])
def call_testHourlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByYearDayNeg()

@app.route('/testHourlyByMonthAndYearDay', methods=['POST'])
def call_testHourlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndYearDay()

@app.route('/testHourlyByMonthAndYearDayNeg', methods=['POST'])
def call_testHourlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMonthAndYearDayNeg()

@app.route('/testHourlyByWeekNo', methods=['POST'])
def call_testHourlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekNo()

@app.route('/testHourlyByWeekNoAndWeekDay', methods=['POST'])
def call_testHourlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekNoAndWeekDay()

@app.route('/testHourlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testHourlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekNoAndWeekDayLarge()

@app.route('/testHourlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testHourlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekNoAndWeekDayLast()

@app.route('/testHourlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testHourlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByWeekNoAndWeekDay53()

@app.route('/testHourlyByEaster', methods=['POST'])
def call_testHourlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByEaster()

@app.route('/testHourlyByEasterPos', methods=['POST'])
def call_testHourlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByEasterPos()

@app.route('/testHourlyByEasterNeg', methods=['POST'])
def call_testHourlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByEasterNeg()

@app.route('/testHourlyByHour', methods=['POST'])
def call_testHourlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByHour()

@app.route('/testHourlyByMinute', methods=['POST'])
def call_testHourlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMinute()

@app.route('/testHourlyBySecond', methods=['POST'])
def call_testHourlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyBySecond()

@app.route('/testHourlyByHourAndMinute', methods=['POST'])
def call_testHourlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByHourAndMinute()

@app.route('/testHourlyByHourAndSecond', methods=['POST'])
def call_testHourlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByHourAndSecond()

@app.route('/testHourlyByMinuteAndSecond', methods=['POST'])
def call_testHourlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByMinuteAndSecond()

@app.route('/testHourlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testHourlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyByHourAndMinuteAndSecond()

@app.route('/testHourlyBySetPos', methods=['POST'])
def call_testHourlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyBySetPos()

@app.route('/testMinutely', methods=['POST'])
def call_testMinutely():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutely()

@app.route('/testMinutelyInterval', methods=['POST'])
def call_testMinutelyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyInterval()

@app.route('/testMinutelyIntervalLarge', methods=['POST'])
def call_testMinutelyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyIntervalLarge()

@app.route('/testMinutelyByMonth', methods=['POST'])
def call_testMinutelyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonth()

@app.route('/testMinutelyByMonthDay', methods=['POST'])
def call_testMinutelyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthDay()

@app.route('/testMinutelyByMonthAndMonthDay', methods=['POST'])
def call_testMinutelyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndMonthDay()

@app.route('/testMinutelyByWeekDay', methods=['POST'])
def call_testMinutelyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekDay()

@app.route('/testMinutelyByNWeekDay', methods=['POST'])
def call_testMinutelyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByNWeekDay()

@app.route('/testMinutelyByMonthAndWeekDay', methods=['POST'])
def call_testMinutelyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndWeekDay()

@app.route('/testMinutelyByMonthAndNWeekDay', methods=['POST'])
def call_testMinutelyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndNWeekDay()

@app.route('/testMinutelyByMonthDayAndWeekDay', methods=['POST'])
def call_testMinutelyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthDayAndWeekDay()

@app.route('/testMinutelyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testMinutelyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndMonthDayAndWeekDay()

@app.route('/testMinutelyByYearDay', methods=['POST'])
def call_testMinutelyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByYearDay()

@app.route('/testMinutelyByYearDayNeg', methods=['POST'])
def call_testMinutelyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByYearDayNeg()

@app.route('/testMinutelyByMonthAndYearDay', methods=['POST'])
def call_testMinutelyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndYearDay()

@app.route('/testMinutelyByMonthAndYearDayNeg', methods=['POST'])
def call_testMinutelyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMonthAndYearDayNeg()

@app.route('/testMinutelyByWeekNo', methods=['POST'])
def call_testMinutelyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekNo()

@app.route('/testMinutelyByWeekNoAndWeekDay', methods=['POST'])
def call_testMinutelyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekNoAndWeekDay()

@app.route('/testMinutelyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testMinutelyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekNoAndWeekDayLarge()

@app.route('/testMinutelyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testMinutelyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekNoAndWeekDayLast()

@app.route('/testMinutelyByWeekNoAndWeekDay53', methods=['POST'])
def call_testMinutelyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByWeekNoAndWeekDay53()

@app.route('/testMinutelyByEaster', methods=['POST'])
def call_testMinutelyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByEaster()

@app.route('/testMinutelyByEasterPos', methods=['POST'])
def call_testMinutelyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByEasterPos()

@app.route('/testMinutelyByEasterNeg', methods=['POST'])
def call_testMinutelyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByEasterNeg()

@app.route('/testMinutelyByHour', methods=['POST'])
def call_testMinutelyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByHour()

@app.route('/testMinutelyByMinute', methods=['POST'])
def call_testMinutelyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMinute()

@app.route('/testMinutelyBySecond', methods=['POST'])
def call_testMinutelyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyBySecond()

@app.route('/testMinutelyByHourAndMinute', methods=['POST'])
def call_testMinutelyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByHourAndMinute()

@app.route('/testMinutelyByHourAndSecond', methods=['POST'])
def call_testMinutelyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByHourAndSecond()

@app.route('/testMinutelyByMinuteAndSecond', methods=['POST'])
def call_testMinutelyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByMinuteAndSecond()

@app.route('/testMinutelyByHourAndMinuteAndSecond', methods=['POST'])
def call_testMinutelyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyByHourAndMinuteAndSecond()

@app.route('/testMinutelyBySetPos', methods=['POST'])
def call_testMinutelyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyBySetPos()

@app.route('/testSecondly', methods=['POST'])
def call_testSecondly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondly()

@app.route('/testSecondlyInterval', methods=['POST'])
def call_testSecondlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyInterval()

@app.route('/testSecondlyIntervalLarge', methods=['POST'])
def call_testSecondlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyIntervalLarge()

@app.route('/testSecondlyByMonth', methods=['POST'])
def call_testSecondlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonth()

@app.route('/testSecondlyByMonthDay', methods=['POST'])
def call_testSecondlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthDay()

@app.route('/testSecondlyByMonthAndMonthDay', methods=['POST'])
def call_testSecondlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndMonthDay()

@app.route('/testSecondlyByWeekDay', methods=['POST'])
def call_testSecondlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekDay()

@app.route('/testSecondlyByNWeekDay', methods=['POST'])
def call_testSecondlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByNWeekDay()

@app.route('/testSecondlyByMonthAndWeekDay', methods=['POST'])
def call_testSecondlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndWeekDay()

@app.route('/testSecondlyByMonthAndNWeekDay', methods=['POST'])
def call_testSecondlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndNWeekDay()

@app.route('/testSecondlyByMonthDayAndWeekDay', methods=['POST'])
def call_testSecondlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthDayAndWeekDay()

@app.route('/testSecondlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testSecondlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndMonthDayAndWeekDay()

@app.route('/testSecondlyByYearDay', methods=['POST'])
def call_testSecondlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByYearDay()

@app.route('/testSecondlyByYearDayNeg', methods=['POST'])
def call_testSecondlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByYearDayNeg()

@app.route('/testSecondlyByMonthAndYearDay', methods=['POST'])
def call_testSecondlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndYearDay()

@app.route('/testSecondlyByMonthAndYearDayNeg', methods=['POST'])
def call_testSecondlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMonthAndYearDayNeg()

@app.route('/testSecondlyByWeekNo', methods=['POST'])
def call_testSecondlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekNo()

@app.route('/testSecondlyByWeekNoAndWeekDay', methods=['POST'])
def call_testSecondlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekNoAndWeekDay()

@app.route('/testSecondlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testSecondlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekNoAndWeekDayLarge()

@app.route('/testSecondlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testSecondlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekNoAndWeekDayLast()

@app.route('/testSecondlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testSecondlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByWeekNoAndWeekDay53()

@app.route('/testSecondlyByEaster', methods=['POST'])
def call_testSecondlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByEaster()

@app.route('/testSecondlyByEasterPos', methods=['POST'])
def call_testSecondlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByEasterPos()

@app.route('/testSecondlyByEasterNeg', methods=['POST'])
def call_testSecondlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByEasterNeg()

@app.route('/testSecondlyByHour', methods=['POST'])
def call_testSecondlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByHour()

@app.route('/testSecondlyByMinute', methods=['POST'])
def call_testSecondlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMinute()

@app.route('/testSecondlyBySecond', methods=['POST'])
def call_testSecondlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyBySecond()

@app.route('/testSecondlyByHourAndMinute', methods=['POST'])
def call_testSecondlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByHourAndMinute()

@app.route('/testSecondlyByHourAndSecond', methods=['POST'])
def call_testSecondlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByHourAndSecond()

@app.route('/testSecondlyByMinuteAndSecond', methods=['POST'])
def call_testSecondlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByMinuteAndSecond()

@app.route('/testSecondlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testSecondlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByHourAndMinuteAndSecond()

@app.route('/testSecondlyByHourAndMinuteAndSecondBug', methods=['POST'])
def call_testSecondlyByHourAndMinuteAndSecondBug():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyByHourAndMinuteAndSecondBug()

@app.route('/testLongIntegers', methods=['POST'])
def call_testLongIntegers():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testLongIntegers()

@app.route('/testHourlyBadRRule', methods=['POST'])
def call_testHourlyBadRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testHourlyBadRRule()

@app.route('/testMinutelyBadRRule', methods=['POST'])
def call_testMinutelyBadRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyBadRRule()

@app.route('/testSecondlyBadRRule', methods=['POST'])
def call_testSecondlyBadRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyBadRRule()

@app.route('/testMinutelyBadComboRRule', methods=['POST'])
def call_testMinutelyBadComboRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMinutelyBadComboRRule()

@app.route('/testSecondlyBadComboRRule', methods=['POST'])
def call_testSecondlyBadComboRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSecondlyBadComboRRule()

@app.route('/testBadUntilCountRRule', methods=['POST'])
def call_testBadUntilCountRRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBadUntilCountRRule()

@app.route('/testUntilNotMatching', methods=['POST'])
def call_testUntilNotMatching():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUntilNotMatching()

@app.route('/testUntilMatching', methods=['POST'])
def call_testUntilMatching():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUntilMatching()

@app.route('/testUntilSingle', methods=['POST'])
def call_testUntilSingle():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUntilSingle()

@app.route('/testUntilEmpty', methods=['POST'])
def call_testUntilEmpty():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUntilEmpty()

@app.route('/testUntilWithDate', methods=['POST'])
def call_testUntilWithDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testUntilWithDate()

@app.route('/testWkStIntervalMO', methods=['POST'])
def call_testWkStIntervalMO():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWkStIntervalMO()

@app.route('/testWkStIntervalSU', methods=['POST'])
def call_testWkStIntervalSU():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWkStIntervalSU()

@app.route('/testDTStartIsDate', methods=['POST'])
def call_testDTStartIsDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDTStartIsDate()

@app.route('/testDTStartWithMicroseconds', methods=['POST'])
def call_testDTStartWithMicroseconds():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testDTStartWithMicroseconds()

@app.route('/testMaxYear', methods=['POST'])
def call_testMaxYear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testMaxYear()

@app.route('/testGetItem', methods=['POST'])
def call_testGetItem():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetItem()

@app.route('/testGetItemNeg', methods=['POST'])
def call_testGetItemNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetItemNeg()

@app.route('/testGetItemSlice', methods=['POST'])
def call_testGetItemSlice():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetItemSlice()

@app.route('/testGetItemSliceEmpty', methods=['POST'])
def call_testGetItemSliceEmpty():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetItemSliceEmpty()

@app.route('/testGetItemSliceStep', methods=['POST'])
def call_testGetItemSliceStep():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testGetItemSliceStep()

@app.route('/testCount', methods=['POST'])
def call_testCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCount()

@app.route('/testCountZero', methods=['POST'])
def call_testCountZero():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCountZero()

@app.route('/testContains', methods=['POST'])
def call_testContains():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testContains()

@app.route('/testContainsNot', methods=['POST'])
def call_testContainsNot():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testContainsNot()

@app.route('/testBefore', methods=['POST'])
def call_testBefore():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBefore()

@app.route('/testBeforeInc', methods=['POST'])
def call_testBeforeInc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBeforeInc()

@app.route('/testAfter', methods=['POST'])
def call_testAfter():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAfter()

@app.route('/testAfterInc', methods=['POST'])
def call_testAfterInc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testAfterInc()

@app.route('/testXAfter', methods=['POST'])
def call_testXAfter():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testXAfter()

@app.route('/testXAfterInc', methods=['POST'])
def call_testXAfterInc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testXAfterInc()

@app.route('/testBetween', methods=['POST'])
def call_testBetween():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBetween()

@app.route('/testBetweenInc', methods=['POST'])
def call_testBetweenInc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBetweenInc()

@app.route('/testCachePre', methods=['POST'])
def call_testCachePre():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCachePre()

@app.route('/testCachePost', methods=['POST'])
def call_testCachePost():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCachePost()

@app.route('/testCachePostInternal', methods=['POST'])
def call_testCachePostInternal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCachePostInternal()

@app.route('/testCachePreContains', methods=['POST'])
def call_testCachePreContains():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCachePreContains()

@app.route('/testCachePostContains', methods=['POST'])
def call_testCachePostContains():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testCachePostContains()

@app.route('/testStr', methods=['POST'])
def call_testStr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStr()

@app.route('/testStrWithTZID', methods=['POST'])
def call_testStrWithTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrWithTZID()

@app.route('/testStrWithTZIDMapping', methods=['POST'])
def call_testStrWithTZIDMapping():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrWithTZIDMapping()

@app.route('/testStrWithTZIDCallable', methods=['POST'])
def call_testStrWithTZIDCallable():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrWithTZIDCallable()

@app.route('/testStrWithTZIDCallableFailure', methods=['POST'])
def call_testStrWithTZIDCallableFailure():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrWithTZIDCallableFailure()

@app.route('/testStrWithConflictingTZID', methods=['POST'])
def call_testStrWithConflictingTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrWithConflictingTZID()

@app.route('/testStrType', methods=['POST'])
def call_testStrType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrType()

@app.route('/testStrForceSetType', methods=['POST'])
def call_testStrForceSetType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrForceSetType()

@app.route('/testStrSetType', methods=['POST'])
def call_testStrSetType():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetType()

@app.route('/testStrCase', methods=['POST'])
def call_testStrCase():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrCase()

@app.route('/testStrSpaces', methods=['POST'])
def call_testStrSpaces():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSpaces()

@app.route('/testStrSpacesAndLines', methods=['POST'])
def call_testStrSpacesAndLines():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSpacesAndLines()

@app.route('/testStrNoDTStart', methods=['POST'])
def call_testStrNoDTStart():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrNoDTStart()

@app.route('/testStrValueOnly', methods=['POST'])
def call_testStrValueOnly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrValueOnly()

@app.route('/testStrUnfold', methods=['POST'])
def call_testStrUnfold():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrUnfold()

@app.route('/testStrSet', methods=['POST'])
def call_testStrSet():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSet()

@app.route('/testStrSetDate', methods=['POST'])
def call_testStrSetDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetDate()

@app.route('/testStrSetExRule', methods=['POST'])
def call_testStrSetExRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExRule()

@app.route('/testStrSetExDate', methods=['POST'])
def call_testStrSetExDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDate()

@app.route('/testStrSetExDateMultiple', methods=['POST'])
def call_testStrSetExDateMultiple():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateMultiple()

@app.route('/testStrSetExDateWithTZID', methods=['POST'])
def call_testStrSetExDateWithTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateWithTZID()

@app.route('/testStrSetExDateValueDateTimeNoTZID', methods=['POST'])
def call_testStrSetExDateValueDateTimeNoTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateValueDateTimeNoTZID()

@app.route('/testStrSetExDateValueMixDateTimeNoTZID', methods=['POST'])
def call_testStrSetExDateValueMixDateTimeNoTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateValueMixDateTimeNoTZID()

@app.route('/testStrSetExDateValueDateTimeWithTZID', methods=['POST'])
def call_testStrSetExDateValueDateTimeWithTZID():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateValueDateTimeWithTZID()

@app.route('/testStrSetExDateValueDate', methods=['POST'])
def call_testStrSetExDateValueDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetExDateValueDate()

@app.route('/testStrSetDateAndExDate', methods=['POST'])
def call_testStrSetDateAndExDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetDateAndExDate()

@app.route('/testStrSetDateAndExRule', methods=['POST'])
def call_testStrSetDateAndExRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrSetDateAndExRule()

@app.route('/testStrKeywords', methods=['POST'])
def call_testStrKeywords():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrKeywords()

@app.route('/testStrNWeekDay', methods=['POST'])
def call_testStrNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrNWeekDay()

@app.route('/testStrUntil', methods=['POST'])
def call_testStrUntil():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrUntil()

@app.route('/testStrValueDatetime', methods=['POST'])
def call_testStrValueDatetime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrValueDatetime()

@app.route('/testStrValueDate', methods=['POST'])
def call_testStrValueDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrValueDate()

@app.route('/testStrMultipleDTStartComma', methods=['POST'])
def call_testStrMultipleDTStartComma():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrMultipleDTStartComma()

@app.route('/testStrInvalidUntil', methods=['POST'])
def call_testStrInvalidUntil():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrInvalidUntil()

@app.route('/testStrUntilMustBeUTC', methods=['POST'])
def call_testStrUntilMustBeUTC():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrUntilMustBeUTC()

@app.route('/testStrUntilWithTZ', methods=['POST'])
def call_testStrUntilWithTZ():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrUntilWithTZ()

@app.route('/testStrEmptyByDay', methods=['POST'])
def call_testStrEmptyByDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrEmptyByDay()

@app.route('/testStrInvalidByDay', methods=['POST'])
def call_testStrInvalidByDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testStrInvalidByDay()

@app.route('/testBadBySetPos', methods=['POST'])
def call_testBadBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBadBySetPos()

@app.route('/testBadBySetPosMany', methods=['POST'])
def call_testBadBySetPosMany():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testBadBySetPosMany()

@app.route('/testToStrYearly', methods=['POST'])
def call_testToStrYearly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearly()

@app.route('/testToStrYearlyInterval', methods=['POST'])
def call_testToStrYearlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyInterval()

@app.route('/testToStrYearlyByMonth', methods=['POST'])
def call_testToStrYearlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonth()

@app.route('/testToStrYearlyByMonthDay', methods=['POST'])
def call_testToStrYearlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthDay()

@app.route('/testToStrYearlyByMonthAndMonthDay', methods=['POST'])
def call_testToStrYearlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndMonthDay()

@app.route('/testToStrYearlyByWeekDay', methods=['POST'])
def call_testToStrYearlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekDay()

@app.route('/testToStrYearlyByNWeekDay', methods=['POST'])
def call_testToStrYearlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByNWeekDay()

@app.route('/testToStrYearlyByNWeekDayLarge', methods=['POST'])
def call_testToStrYearlyByNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByNWeekDayLarge()

@app.route('/testToStrYearlyByMonthAndWeekDay', methods=['POST'])
def call_testToStrYearlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndWeekDay()

@app.route('/testToStrYearlyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrYearlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndNWeekDay()

@app.route('/testToStrYearlyByMonthAndNWeekDayLarge', methods=['POST'])
def call_testToStrYearlyByMonthAndNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndNWeekDayLarge()

@app.route('/testToStrYearlyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrYearlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthDayAndWeekDay()

@app.route('/testToStrYearlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrYearlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrYearlyByYearDay', methods=['POST'])
def call_testToStrYearlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByYearDay()

@app.route('/testToStrYearlyByYearDayNeg', methods=['POST'])
def call_testToStrYearlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByYearDayNeg()

@app.route('/testToStrYearlyByMonthAndYearDay', methods=['POST'])
def call_testToStrYearlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndYearDay()

@app.route('/testToStrYearlyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrYearlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMonthAndYearDayNeg()

@app.route('/testToStrYearlyByWeekNo', methods=['POST'])
def call_testToStrYearlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekNo()

@app.route('/testToStrYearlyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrYearlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekNoAndWeekDay()

@app.route('/testToStrYearlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrYearlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekNoAndWeekDayLarge()

@app.route('/testToStrYearlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrYearlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekNoAndWeekDayLast()

@app.route('/testToStrYearlyByEaster', methods=['POST'])
def call_testToStrYearlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByEaster()

@app.route('/testToStrYearlyByEasterPos', methods=['POST'])
def call_testToStrYearlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByEasterPos()

@app.route('/testToStrYearlyByEasterNeg', methods=['POST'])
def call_testToStrYearlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByEasterNeg()

@app.route('/testToStrYearlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrYearlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByWeekNoAndWeekDay53()

@app.route('/testToStrYearlyByHour', methods=['POST'])
def call_testToStrYearlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByHour()

@app.route('/testToStrYearlyByMinute', methods=['POST'])
def call_testToStrYearlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMinute()

@app.route('/testToStrYearlyBySecond', methods=['POST'])
def call_testToStrYearlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyBySecond()

@app.route('/testToStrYearlyByHourAndMinute', methods=['POST'])
def call_testToStrYearlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByHourAndMinute()

@app.route('/testToStrYearlyByHourAndSecond', methods=['POST'])
def call_testToStrYearlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByHourAndSecond()

@app.route('/testToStrYearlyByMinuteAndSecond', methods=['POST'])
def call_testToStrYearlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByMinuteAndSecond()

@app.route('/testToStrYearlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrYearlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyByHourAndMinuteAndSecond()

@app.route('/testToStrYearlyBySetPos', methods=['POST'])
def call_testToStrYearlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrYearlyBySetPos()

@app.route('/testToStrMonthly', methods=['POST'])
def call_testToStrMonthly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthly()

@app.route('/testToStrMonthlyInterval', methods=['POST'])
def call_testToStrMonthlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyInterval()

@app.route('/testToStrMonthlyIntervalLarge', methods=['POST'])
def call_testToStrMonthlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyIntervalLarge()

@app.route('/testToStrMonthlyByMonth', methods=['POST'])
def call_testToStrMonthlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonth()

@app.route('/testToStrMonthlyByMonthDay', methods=['POST'])
def call_testToStrMonthlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthDay()

@app.route('/testToStrMonthlyByMonthAndMonthDay', methods=['POST'])
def call_testToStrMonthlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndMonthDay()

@app.route('/testToStrMonthlyByWeekDay', methods=['POST'])
def call_testToStrMonthlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekDay()

@app.route('/testToStrMonthlyByNWeekDay', methods=['POST'])
def call_testToStrMonthlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByNWeekDay()

@app.route('/testToStrMonthlyByNWeekDayLarge', methods=['POST'])
def call_testToStrMonthlyByNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByNWeekDayLarge()

@app.route('/testToStrMonthlyByMonthAndWeekDay', methods=['POST'])
def call_testToStrMonthlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndWeekDay()

@app.route('/testToStrMonthlyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrMonthlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndNWeekDay()

@app.route('/testToStrMonthlyByMonthAndNWeekDayLarge', methods=['POST'])
def call_testToStrMonthlyByMonthAndNWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndNWeekDayLarge()

@app.route('/testToStrMonthlyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrMonthlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthDayAndWeekDay()

@app.route('/testToStrMonthlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrMonthlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrMonthlyByYearDay', methods=['POST'])
def call_testToStrMonthlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByYearDay()

@app.route('/testToStrMonthlyByYearDayNeg', methods=['POST'])
def call_testToStrMonthlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByYearDayNeg()

@app.route('/testToStrMonthlyByMonthAndYearDay', methods=['POST'])
def call_testToStrMonthlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndYearDay()

@app.route('/testToStrMonthlyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrMonthlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMonthAndYearDayNeg()

@app.route('/testToStrMonthlyByWeekNo', methods=['POST'])
def call_testToStrMonthlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekNo()

@app.route('/testToStrMonthlyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrMonthlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekNoAndWeekDay()

@app.route('/testToStrMonthlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrMonthlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekNoAndWeekDayLarge()

@app.route('/testToStrMonthlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrMonthlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekNoAndWeekDayLast()

@app.route('/testToStrMonthlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrMonthlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByWeekNoAndWeekDay53()

@app.route('/testToStrMonthlyByEaster', methods=['POST'])
def call_testToStrMonthlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByEaster()

@app.route('/testToStrMonthlyByEasterPos', methods=['POST'])
def call_testToStrMonthlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByEasterPos()

@app.route('/testToStrMonthlyByEasterNeg', methods=['POST'])
def call_testToStrMonthlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByEasterNeg()

@app.route('/testToStrMonthlyByHour', methods=['POST'])
def call_testToStrMonthlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByHour()

@app.route('/testToStrMonthlyByMinute', methods=['POST'])
def call_testToStrMonthlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMinute()

@app.route('/testToStrMonthlyBySecond', methods=['POST'])
def call_testToStrMonthlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyBySecond()

@app.route('/testToStrMonthlyByHourAndMinute', methods=['POST'])
def call_testToStrMonthlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByHourAndMinute()

@app.route('/testToStrMonthlyByHourAndSecond', methods=['POST'])
def call_testToStrMonthlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByHourAndSecond()

@app.route('/testToStrMonthlyByMinuteAndSecond', methods=['POST'])
def call_testToStrMonthlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByMinuteAndSecond()

@app.route('/testToStrMonthlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrMonthlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyByHourAndMinuteAndSecond()

@app.route('/testToStrMonthlyBySetPos', methods=['POST'])
def call_testToStrMonthlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMonthlyBySetPos()

@app.route('/testToStrWeekly', methods=['POST'])
def call_testToStrWeekly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeekly()

@app.route('/testToStrWeeklyInterval', methods=['POST'])
def call_testToStrWeeklyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyInterval()

@app.route('/testToStrWeeklyIntervalLarge', methods=['POST'])
def call_testToStrWeeklyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyIntervalLarge()

@app.route('/testToStrWeeklyByMonth', methods=['POST'])
def call_testToStrWeeklyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonth()

@app.route('/testToStrWeeklyByMonthDay', methods=['POST'])
def call_testToStrWeeklyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthDay()

@app.route('/testToStrWeeklyByMonthAndMonthDay', methods=['POST'])
def call_testToStrWeeklyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndMonthDay()

@app.route('/testToStrWeeklyByWeekDay', methods=['POST'])
def call_testToStrWeeklyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekDay()

@app.route('/testToStrWeeklyByNWeekDay', methods=['POST'])
def call_testToStrWeeklyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByNWeekDay()

@app.route('/testToStrWeeklyByMonthAndWeekDay', methods=['POST'])
def call_testToStrWeeklyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndWeekDay()

@app.route('/testToStrWeeklyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrWeeklyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndNWeekDay()

@app.route('/testToStrWeeklyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrWeeklyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthDayAndWeekDay()

@app.route('/testToStrWeeklyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrWeeklyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrWeeklyByYearDay', methods=['POST'])
def call_testToStrWeeklyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByYearDay()

@app.route('/testToStrWeeklyByYearDayNeg', methods=['POST'])
def call_testToStrWeeklyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByYearDayNeg()

@app.route('/testToStrWeeklyByMonthAndYearDay', methods=['POST'])
def call_testToStrWeeklyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndYearDay()

@app.route('/testToStrWeeklyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrWeeklyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMonthAndYearDayNeg()

@app.route('/testToStrWeeklyByWeekNo', methods=['POST'])
def call_testToStrWeeklyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekNo()

@app.route('/testToStrWeeklyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrWeeklyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekNoAndWeekDay()

@app.route('/testToStrWeeklyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrWeeklyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekNoAndWeekDayLarge()

@app.route('/testToStrWeeklyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrWeeklyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekNoAndWeekDayLast()

@app.route('/testToStrWeeklyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrWeeklyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByWeekNoAndWeekDay53()

@app.route('/testToStrWeeklyByEaster', methods=['POST'])
def call_testToStrWeeklyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByEaster()

@app.route('/testToStrWeeklyByEasterPos', methods=['POST'])
def call_testToStrWeeklyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByEasterPos()

@app.route('/testToStrWeeklyByEasterNeg', methods=['POST'])
def call_testToStrWeeklyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByEasterNeg()

@app.route('/testToStrWeeklyByHour', methods=['POST'])
def call_testToStrWeeklyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByHour()

@app.route('/testToStrWeeklyByMinute', methods=['POST'])
def call_testToStrWeeklyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMinute()

@app.route('/testToStrWeeklyBySecond', methods=['POST'])
def call_testToStrWeeklyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyBySecond()

@app.route('/testToStrWeeklyByHourAndMinute', methods=['POST'])
def call_testToStrWeeklyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByHourAndMinute()

@app.route('/testToStrWeeklyByHourAndSecond', methods=['POST'])
def call_testToStrWeeklyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByHourAndSecond()

@app.route('/testToStrWeeklyByMinuteAndSecond', methods=['POST'])
def call_testToStrWeeklyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByMinuteAndSecond()

@app.route('/testToStrWeeklyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrWeeklyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyByHourAndMinuteAndSecond()

@app.route('/testToStrWeeklyBySetPos', methods=['POST'])
def call_testToStrWeeklyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWeeklyBySetPos()

@app.route('/testToStrDaily', methods=['POST'])
def call_testToStrDaily():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDaily()

@app.route('/testToStrDailyInterval', methods=['POST'])
def call_testToStrDailyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyInterval()

@app.route('/testToStrDailyIntervalLarge', methods=['POST'])
def call_testToStrDailyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyIntervalLarge()

@app.route('/testToStrDailyByMonth', methods=['POST'])
def call_testToStrDailyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonth()

@app.route('/testToStrDailyByMonthDay', methods=['POST'])
def call_testToStrDailyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthDay()

@app.route('/testToStrDailyByMonthAndMonthDay', methods=['POST'])
def call_testToStrDailyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndMonthDay()

@app.route('/testToStrDailyByWeekDay', methods=['POST'])
def call_testToStrDailyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekDay()

@app.route('/testToStrDailyByNWeekDay', methods=['POST'])
def call_testToStrDailyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByNWeekDay()

@app.route('/testToStrDailyByMonthAndWeekDay', methods=['POST'])
def call_testToStrDailyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndWeekDay()

@app.route('/testToStrDailyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrDailyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndNWeekDay()

@app.route('/testToStrDailyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrDailyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthDayAndWeekDay()

@app.route('/testToStrDailyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrDailyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrDailyByYearDay', methods=['POST'])
def call_testToStrDailyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByYearDay()

@app.route('/testToStrDailyByYearDayNeg', methods=['POST'])
def call_testToStrDailyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByYearDayNeg()

@app.route('/testToStrDailyByMonthAndYearDay', methods=['POST'])
def call_testToStrDailyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndYearDay()

@app.route('/testToStrDailyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrDailyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMonthAndYearDayNeg()

@app.route('/testToStrDailyByWeekNo', methods=['POST'])
def call_testToStrDailyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekNo()

@app.route('/testToStrDailyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrDailyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekNoAndWeekDay()

@app.route('/testToStrDailyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrDailyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekNoAndWeekDayLarge()

@app.route('/testToStrDailyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrDailyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekNoAndWeekDayLast()

@app.route('/testToStrDailyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrDailyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByWeekNoAndWeekDay53()

@app.route('/testToStrDailyByEaster', methods=['POST'])
def call_testToStrDailyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByEaster()

@app.route('/testToStrDailyByEasterPos', methods=['POST'])
def call_testToStrDailyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByEasterPos()

@app.route('/testToStrDailyByEasterNeg', methods=['POST'])
def call_testToStrDailyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByEasterNeg()

@app.route('/testToStrDailyByHour', methods=['POST'])
def call_testToStrDailyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByHour()

@app.route('/testToStrDailyByMinute', methods=['POST'])
def call_testToStrDailyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMinute()

@app.route('/testToStrDailyBySecond', methods=['POST'])
def call_testToStrDailyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyBySecond()

@app.route('/testToStrDailyByHourAndMinute', methods=['POST'])
def call_testToStrDailyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByHourAndMinute()

@app.route('/testToStrDailyByHourAndSecond', methods=['POST'])
def call_testToStrDailyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByHourAndSecond()

@app.route('/testToStrDailyByMinuteAndSecond', methods=['POST'])
def call_testToStrDailyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByMinuteAndSecond()

@app.route('/testToStrDailyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrDailyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyByHourAndMinuteAndSecond()

@app.route('/testToStrDailyBySetPos', methods=['POST'])
def call_testToStrDailyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrDailyBySetPos()

@app.route('/testToStrHourly', methods=['POST'])
def call_testToStrHourly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourly()

@app.route('/testToStrHourlyInterval', methods=['POST'])
def call_testToStrHourlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyInterval()

@app.route('/testToStrHourlyIntervalLarge', methods=['POST'])
def call_testToStrHourlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyIntervalLarge()

@app.route('/testToStrHourlyByMonth', methods=['POST'])
def call_testToStrHourlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonth()

@app.route('/testToStrHourlyByMonthDay', methods=['POST'])
def call_testToStrHourlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthDay()

@app.route('/testToStrHourlyByMonthAndMonthDay', methods=['POST'])
def call_testToStrHourlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndMonthDay()

@app.route('/testToStrHourlyByWeekDay', methods=['POST'])
def call_testToStrHourlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekDay()

@app.route('/testToStrHourlyByNWeekDay', methods=['POST'])
def call_testToStrHourlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByNWeekDay()

@app.route('/testToStrHourlyByMonthAndWeekDay', methods=['POST'])
def call_testToStrHourlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndWeekDay()

@app.route('/testToStrHourlyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrHourlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndNWeekDay()

@app.route('/testToStrHourlyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrHourlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthDayAndWeekDay()

@app.route('/testToStrHourlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrHourlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrHourlyByYearDay', methods=['POST'])
def call_testToStrHourlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByYearDay()

@app.route('/testToStrHourlyByYearDayNeg', methods=['POST'])
def call_testToStrHourlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByYearDayNeg()

@app.route('/testToStrHourlyByMonthAndYearDay', methods=['POST'])
def call_testToStrHourlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndYearDay()

@app.route('/testToStrHourlyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrHourlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMonthAndYearDayNeg()

@app.route('/testToStrHourlyByWeekNo', methods=['POST'])
def call_testToStrHourlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekNo()

@app.route('/testToStrHourlyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrHourlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekNoAndWeekDay()

@app.route('/testToStrHourlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrHourlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekNoAndWeekDayLarge()

@app.route('/testToStrHourlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrHourlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekNoAndWeekDayLast()

@app.route('/testToStrHourlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrHourlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByWeekNoAndWeekDay53()

@app.route('/testToStrHourlyByEaster', methods=['POST'])
def call_testToStrHourlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByEaster()

@app.route('/testToStrHourlyByEasterPos', methods=['POST'])
def call_testToStrHourlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByEasterPos()

@app.route('/testToStrHourlyByEasterNeg', methods=['POST'])
def call_testToStrHourlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByEasterNeg()

@app.route('/testToStrHourlyByHour', methods=['POST'])
def call_testToStrHourlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByHour()

@app.route('/testToStrHourlyByMinute', methods=['POST'])
def call_testToStrHourlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMinute()

@app.route('/testToStrHourlyBySecond', methods=['POST'])
def call_testToStrHourlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyBySecond()

@app.route('/testToStrHourlyByHourAndMinute', methods=['POST'])
def call_testToStrHourlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByHourAndMinute()

@app.route('/testToStrHourlyByHourAndSecond', methods=['POST'])
def call_testToStrHourlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByHourAndSecond()

@app.route('/testToStrHourlyByMinuteAndSecond', methods=['POST'])
def call_testToStrHourlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByMinuteAndSecond()

@app.route('/testToStrHourlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrHourlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyByHourAndMinuteAndSecond()

@app.route('/testToStrHourlyBySetPos', methods=['POST'])
def call_testToStrHourlyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrHourlyBySetPos()

@app.route('/testToStrMinutely', methods=['POST'])
def call_testToStrMinutely():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutely()

@app.route('/testToStrMinutelyInterval', methods=['POST'])
def call_testToStrMinutelyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyInterval()

@app.route('/testToStrMinutelyIntervalLarge', methods=['POST'])
def call_testToStrMinutelyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyIntervalLarge()

@app.route('/testToStrMinutelyByMonth', methods=['POST'])
def call_testToStrMinutelyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonth()

@app.route('/testToStrMinutelyByMonthDay', methods=['POST'])
def call_testToStrMinutelyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthDay()

@app.route('/testToStrMinutelyByMonthAndMonthDay', methods=['POST'])
def call_testToStrMinutelyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndMonthDay()

@app.route('/testToStrMinutelyByWeekDay', methods=['POST'])
def call_testToStrMinutelyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekDay()

@app.route('/testToStrMinutelyByNWeekDay', methods=['POST'])
def call_testToStrMinutelyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByNWeekDay()

@app.route('/testToStrMinutelyByMonthAndWeekDay', methods=['POST'])
def call_testToStrMinutelyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndWeekDay()

@app.route('/testToStrMinutelyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrMinutelyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndNWeekDay()

@app.route('/testToStrMinutelyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrMinutelyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthDayAndWeekDay()

@app.route('/testToStrMinutelyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrMinutelyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrMinutelyByYearDay', methods=['POST'])
def call_testToStrMinutelyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByYearDay()

@app.route('/testToStrMinutelyByYearDayNeg', methods=['POST'])
def call_testToStrMinutelyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByYearDayNeg()

@app.route('/testToStrMinutelyByMonthAndYearDay', methods=['POST'])
def call_testToStrMinutelyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndYearDay()

@app.route('/testToStrMinutelyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrMinutelyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMonthAndYearDayNeg()

@app.route('/testToStrMinutelyByWeekNo', methods=['POST'])
def call_testToStrMinutelyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekNo()

@app.route('/testToStrMinutelyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrMinutelyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekNoAndWeekDay()

@app.route('/testToStrMinutelyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrMinutelyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekNoAndWeekDayLarge()

@app.route('/testToStrMinutelyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrMinutelyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekNoAndWeekDayLast()

@app.route('/testToStrMinutelyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrMinutelyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByWeekNoAndWeekDay53()

@app.route('/testToStrMinutelyByEaster', methods=['POST'])
def call_testToStrMinutelyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByEaster()

@app.route('/testToStrMinutelyByEasterPos', methods=['POST'])
def call_testToStrMinutelyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByEasterPos()

@app.route('/testToStrMinutelyByEasterNeg', methods=['POST'])
def call_testToStrMinutelyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByEasterNeg()

@app.route('/testToStrMinutelyByHour', methods=['POST'])
def call_testToStrMinutelyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByHour()

@app.route('/testToStrMinutelyByMinute', methods=['POST'])
def call_testToStrMinutelyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMinute()

@app.route('/testToStrMinutelyBySecond', methods=['POST'])
def call_testToStrMinutelyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyBySecond()

@app.route('/testToStrMinutelyByHourAndMinute', methods=['POST'])
def call_testToStrMinutelyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByHourAndMinute()

@app.route('/testToStrMinutelyByHourAndSecond', methods=['POST'])
def call_testToStrMinutelyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByHourAndSecond()

@app.route('/testToStrMinutelyByMinuteAndSecond', methods=['POST'])
def call_testToStrMinutelyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByMinuteAndSecond()

@app.route('/testToStrMinutelyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrMinutelyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyByHourAndMinuteAndSecond()

@app.route('/testToStrMinutelyBySetPos', methods=['POST'])
def call_testToStrMinutelyBySetPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrMinutelyBySetPos()

@app.route('/testToStrSecondly', methods=['POST'])
def call_testToStrSecondly():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondly()

@app.route('/testToStrSecondlyInterval', methods=['POST'])
def call_testToStrSecondlyInterval():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyInterval()

@app.route('/testToStrSecondlyIntervalLarge', methods=['POST'])
def call_testToStrSecondlyIntervalLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyIntervalLarge()

@app.route('/testToStrSecondlyByMonth', methods=['POST'])
def call_testToStrSecondlyByMonth():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonth()

@app.route('/testToStrSecondlyByMonthDay', methods=['POST'])
def call_testToStrSecondlyByMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthDay()

@app.route('/testToStrSecondlyByMonthAndMonthDay', methods=['POST'])
def call_testToStrSecondlyByMonthAndMonthDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndMonthDay()

@app.route('/testToStrSecondlyByWeekDay', methods=['POST'])
def call_testToStrSecondlyByWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekDay()

@app.route('/testToStrSecondlyByNWeekDay', methods=['POST'])
def call_testToStrSecondlyByNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByNWeekDay()

@app.route('/testToStrSecondlyByMonthAndWeekDay', methods=['POST'])
def call_testToStrSecondlyByMonthAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndWeekDay()

@app.route('/testToStrSecondlyByMonthAndNWeekDay', methods=['POST'])
def call_testToStrSecondlyByMonthAndNWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndNWeekDay()

@app.route('/testToStrSecondlyByMonthDayAndWeekDay', methods=['POST'])
def call_testToStrSecondlyByMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthDayAndWeekDay()

@app.route('/testToStrSecondlyByMonthAndMonthDayAndWeekDay', methods=['POST'])
def call_testToStrSecondlyByMonthAndMonthDayAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndMonthDayAndWeekDay()

@app.route('/testToStrSecondlyByYearDay', methods=['POST'])
def call_testToStrSecondlyByYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByYearDay()

@app.route('/testToStrSecondlyByYearDayNeg', methods=['POST'])
def call_testToStrSecondlyByYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByYearDayNeg()

@app.route('/testToStrSecondlyByMonthAndYearDay', methods=['POST'])
def call_testToStrSecondlyByMonthAndYearDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndYearDay()

@app.route('/testToStrSecondlyByMonthAndYearDayNeg', methods=['POST'])
def call_testToStrSecondlyByMonthAndYearDayNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMonthAndYearDayNeg()

@app.route('/testToStrSecondlyByWeekNo', methods=['POST'])
def call_testToStrSecondlyByWeekNo():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekNo()

@app.route('/testToStrSecondlyByWeekNoAndWeekDay', methods=['POST'])
def call_testToStrSecondlyByWeekNoAndWeekDay():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekNoAndWeekDay()

@app.route('/testToStrSecondlyByWeekNoAndWeekDayLarge', methods=['POST'])
def call_testToStrSecondlyByWeekNoAndWeekDayLarge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekNoAndWeekDayLarge()

@app.route('/testToStrSecondlyByWeekNoAndWeekDayLast', methods=['POST'])
def call_testToStrSecondlyByWeekNoAndWeekDayLast():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekNoAndWeekDayLast()

@app.route('/testToStrSecondlyByWeekNoAndWeekDay53', methods=['POST'])
def call_testToStrSecondlyByWeekNoAndWeekDay53():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByWeekNoAndWeekDay53()

@app.route('/testToStrSecondlyByEaster', methods=['POST'])
def call_testToStrSecondlyByEaster():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByEaster()

@app.route('/testToStrSecondlyByEasterPos', methods=['POST'])
def call_testToStrSecondlyByEasterPos():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByEasterPos()

@app.route('/testToStrSecondlyByEasterNeg', methods=['POST'])
def call_testToStrSecondlyByEasterNeg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByEasterNeg()

@app.route('/testToStrSecondlyByHour', methods=['POST'])
def call_testToStrSecondlyByHour():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByHour()

@app.route('/testToStrSecondlyByMinute', methods=['POST'])
def call_testToStrSecondlyByMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMinute()

@app.route('/testToStrSecondlyBySecond', methods=['POST'])
def call_testToStrSecondlyBySecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyBySecond()

@app.route('/testToStrSecondlyByHourAndMinute', methods=['POST'])
def call_testToStrSecondlyByHourAndMinute():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByHourAndMinute()

@app.route('/testToStrSecondlyByHourAndSecond', methods=['POST'])
def call_testToStrSecondlyByHourAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByHourAndSecond()

@app.route('/testToStrSecondlyByMinuteAndSecond', methods=['POST'])
def call_testToStrSecondlyByMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByMinuteAndSecond()

@app.route('/testToStrSecondlyByHourAndMinuteAndSecond', methods=['POST'])
def call_testToStrSecondlyByHourAndMinuteAndSecond():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByHourAndMinuteAndSecond()

@app.route('/testToStrSecondlyByHourAndMinuteAndSecondBug', methods=['POST'])
def call_testToStrSecondlyByHourAndMinuteAndSecondBug():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrSecondlyByHourAndMinuteAndSecondBug()

@app.route('/testToStrWithWkSt', methods=['POST'])
def call_testToStrWithWkSt():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrWithWkSt()

@app.route('/testToStrLongIntegers', methods=['POST'])
def call_testToStrLongIntegers():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testToStrLongIntegers()

@app.route('/testReplaceIfSet', methods=['POST'])
def call_testReplaceIfSet():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testReplaceIfSet()

@app.route('/testReplaceIfNotSet', methods=['POST'])
def call_testReplaceIfNotSet():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testReplaceIfNotSet()

@app.route('/test_generated_aware_dtstart', methods=['POST'])
def call_test_generated_aware_dtstart():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_generated_aware_dtstart()

@app.route('/test_generated_aware_dtstart_rrulestr', methods=['POST'])
def call_test_generated_aware_dtstart_rrulestr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_generated_aware_dtstart_rrulestr()

@app.route('/testSet', methods=['POST'])
def call_testSet():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSet()

@app.route('/testSetDate', methods=['POST'])
def call_testSetDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetDate()

@app.route('/testSetExRule', methods=['POST'])
def call_testSetExRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetExRule()

@app.route('/testSetExDate', methods=['POST'])
def call_testSetExDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetExDate()

@app.route('/testSetExDateRevOrder', methods=['POST'])
def call_testSetExDateRevOrder():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetExDateRevOrder()

@app.route('/testSetDateAndExDate', methods=['POST'])
def call_testSetDateAndExDate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetDateAndExDate()

@app.route('/testSetDateAndExRule', methods=['POST'])
def call_testSetDateAndExRule():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetDateAndExRule()

@app.route('/testSetCount', methods=['POST'])
def call_testSetCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetCount()

@app.route('/testSetCachePre', methods=['POST'])
def call_testSetCachePre():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetCachePre()

@app.route('/testSetCachePost', methods=['POST'])
def call_testSetCachePost():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetCachePost()

@app.route('/testSetCachePostInternal', methods=['POST'])
def call_testSetCachePostInternal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetCachePostInternal()

@app.route('/testSetRRuleCount', methods=['POST'])
def call_testSetRRuleCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetRRuleCount()

@app.route('/testSetRDateCount', methods=['POST'])
def call_testSetRDateCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetRDateCount()

@app.route('/testSetExRuleCount', methods=['POST'])
def call_testSetExRuleCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetExRuleCount()

@app.route('/testSetExDateCount', methods=['POST'])
def call_testSetExDateCount():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testSetExDateCount()

@app.route('/testInvalidNthWeekday', methods=['POST'])
def call_testInvalidNthWeekday():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testInvalidNthWeekday()

@app.route('/testWeekdayCallable', methods=['POST'])
def call_testWeekdayCallable():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekdayCallable()

@app.route('/testWeekdayEquality', methods=['POST'])
def call_testWeekdayEquality():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekdayEquality()

@app.route('/testWeekdayEqualitySubclass', methods=['POST'])
def call_testWeekdayEqualitySubclass():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekdayEqualitySubclass()

@app.route('/testWeekdayReprNoN', methods=['POST'])
def call_testWeekdayReprNoN():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekdayReprNoN()

@app.route('/testWeekdayReprWithN', methods=['POST'])
def call_testWeekdayReprWithN():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return testWeekdayReprWithN()

@app.route('/clean_import', methods=['POST'])
def call_clean_import():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return clean_import()

@app.route('/test_lazy_import', methods=['POST'])
def call_test_lazy_import():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    clean_import = request_json.get("clean_import")
    
    module = request_json.get("module")
    

    return test_lazy_import(clean_import, module)

@app.route('/test_import_version_str', methods=['POST'])
def call_test_import_version_str():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_version_str()

@app.route('/test_import_version_root', methods=['POST'])
def call_test_import_version_root():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_version_root()

@app.route('/test_import_easter_direct', methods=['POST'])
def call_test_import_easter_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_easter_direct()

@app.route('/test_import_easter_from', methods=['POST'])
def call_test_import_easter_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_easter_from()

@app.route('/test_import_easter_start', methods=['POST'])
def call_test_import_easter_start():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_easter_start()

@app.route('/test_import_parser_direct', methods=['POST'])
def call_test_import_parser_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_parser_direct()

@app.route('/test_import_parser_from', methods=['POST'])
def call_test_import_parser_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_parser_from()

@app.route('/test_import_parser_all', methods=['POST'])
def call_test_import_parser_all():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_parser_all()

@app.route('/test_import_relative_delta_direct', methods=['POST'])
def call_test_import_relative_delta_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_relative_delta_direct()

@app.route('/test_import_relative_delta_from', methods=['POST'])
def call_test_import_relative_delta_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_relative_delta_from()

@app.route('/test_import_relative_delta_all', methods=['POST'])
def call_test_import_relative_delta_all():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_relative_delta_all()

@app.route('/test_import_rrule_direct', methods=['POST'])
def call_test_import_rrule_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_rrule_direct()

@app.route('/test_import_rrule_from', methods=['POST'])
def call_test_import_rrule_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_rrule_from()

@app.route('/test_import_rrule_all', methods=['POST'])
def call_test_import_rrule_all():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_rrule_all()

@app.route('/test_import_tztest_direct', methods=['POST'])
def call_test_import_tztest_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tztest_direct()

@app.route('/test_import_tz_from', methods=['POST'])
def call_test_import_tz_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tz_from()

@app.route('/test_import_tz_all', methods=['POST'])
def call_test_import_tz_all():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tz_all()

@app.route('/test_import_tz_windows_direct', methods=['POST'])
def call_test_import_tz_windows_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tz_windows_direct()

@app.route('/test_import_tz_windows_from', methods=['POST'])
def call_test_import_tz_windows_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tz_windows_from()

@app.route('/test_import_tz_windows_star', methods=['POST'])
def call_test_import_tz_windows_star():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_tz_windows_star()

@app.route('/test_import_zone_info_direct', methods=['POST'])
def call_test_import_zone_info_direct():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_zone_info_direct()

@app.route('/test_import_zone_info_from', methods=['POST'])
def call_test_import_zone_info_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_zone_info_from()

@app.route('/test_import_zone_info_star', methods=['POST'])
def call_test_import_zone_info_star():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_import_zone_info_star()

@app.route('/test_year_only', methods=['POST'])
def call_test_year_only():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return test_year_only(dt)

@app.route('/test_year_month', methods=['POST'])
def call_test_year_month():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    

    return test_year_month(dt)

@app.route('/test_year_month_day', methods=['POST'])
def call_test_year_month_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    fmt = request_json.get("fmt")
    

    return test_year_month_day(dt, fmt)

@app.route('/test_ymd_h', methods=['POST'])
def call_test_ymd_h():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    date_fmt = request_json.get("date_fmt")
    
    tzoffset = request_json.get("tzoffset")
    

    return test_ymd_h(dt, date_fmt, tzoffset)

@app.route('/test_ymd_hm', methods=['POST'])
def call_test_ymd_hm():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    date_fmt = request_json.get("date_fmt")
    
    time_fmt = request_json.get("time_fmt")
    
    tzoffset = request_json.get("tzoffset")
    

    return test_ymd_hm(dt, date_fmt, time_fmt, tzoffset)

@app.route('/test_ymd_hms', methods=['POST'])
def call_test_ymd_hms():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    date_fmt = request_json.get("date_fmt")
    
    time_fmt = request_json.get("time_fmt")
    
    tzoffset = request_json.get("tzoffset")
    

    return test_ymd_hms(dt, date_fmt, time_fmt, tzoffset)

@app.route('/test_ymd_hms_micro', methods=['POST'])
def call_test_ymd_hms_micro():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    date_fmt = request_json.get("date_fmt")
    
    time_fmt = request_json.get("time_fmt")
    
    tzoffset = request_json.get("tzoffset")
    
    precision = request_json.get("precision")
    

    return test_ymd_hms_micro(dt, date_fmt, time_fmt, tzoffset, precision)

@app.route('/test_extra_subsecond_digits', methods=['POST'])
def call_test_extra_subsecond_digits():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt_str = request_json.get("dt_str")
    

    return test_extra_subsecond_digits(dt_str)

@app.route('/test_full_tzoffsets', methods=['POST'])
def call_test_full_tzoffsets():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzoffset = request_json.get("tzoffset")
    

    return test_full_tzoffsets(tzoffset)

@app.route('/test_datetime_midnight', methods=['POST'])
def call_test_datetime_midnight():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt_str = request_json.get("dt_str")
    

    return test_datetime_midnight(dt_str)

@app.route('/test_isoparse_sep_none', methods=['POST'])
def call_test_isoparse_sep_none():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    datestr = request_json.get("datestr")
    
    sep = request_json.get("sep")
    

    return test_isoparse_sep_none(datestr, sep)

@app.route('/test_isoweek', methods=['POST'])
def call_test_isoweek():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isocal = request_json.get("isocal")
    
    dt_expected = request_json.get("dt_expected")
    

    return test_isoweek(isocal, dt_expected)

@app.route('/test_isoweek_day', methods=['POST'])
def call_test_isoweek_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isocal = request_json.get("isocal")
    
    dt_expected = request_json.get("dt_expected")
    

    return test_isoweek_day(isocal, dt_expected)

@app.route('/test_iso_ordinal', methods=['POST'])
def call_test_iso_ordinal():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isoord = request_json.get("isoord")
    
    dt_expected = request_json.get("dt_expected")
    

    return test_iso_ordinal(isoord, dt_expected)

@app.route('/test_bytes', methods=['POST'])
def call_test_bytes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isostr = request_json.get("isostr")
    
    dt = request_json.get("dt")
    

    return test_bytes(isostr, dt)

@app.route('/test_iso_raises', methods=['POST'])
def call_test_iso_raises():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isostr = request_json.get("isostr")
    
    exception = request_json.get("exception")
    

    return test_iso_raises(isostr, exception)

@app.route('/test_iso_with_sep_raises', methods=['POST'])
def call_test_iso_with_sep_raises():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    sep_act = request_json.get("sep_act")
    
    valid_sep = request_json.get("valid_sep")
    
    exception = request_json.get("exception")
    

    return test_iso_with_sep_raises(sep_act, valid_sep, exception)

@app.route('/test_isoparser_invalid_sep', methods=['POST'])
def call_test_isoparser_invalid_sep():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    sep = request_json.get("sep")
    

    return test_isoparser_invalid_sep(sep)

@app.route('/test_isoparser_byte_sep', methods=['POST'])
def call_test_isoparser_byte_sep():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_isoparser_byte_sep()

@app.route('/test_parse_tzstr', methods=['POST'])
def call_test_parse_tzstr():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzoffset = request_json.get("tzoffset")
    

    return test_parse_tzstr(tzoffset)

@app.route('/test_parse_tzstr_zero_as_utc', methods=['POST'])
def call_test_parse_tzstr_zero_as_utc():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzstr = request_json.get("tzstr")
    
    zero_as_utc = request_json.get("zero_as_utc")
    

    return test_parse_tzstr_zero_as_utc(tzstr, zero_as_utc)

@app.route('/test_parse_tzstr_fails', methods=['POST'])
def call_test_parse_tzstr_fails():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tzstr = request_json.get("tzstr")
    
    exception = request_json.get("exception")
    

    return test_parse_tzstr_fails(tzstr, exception)

@app.route('/test_parse_isodate', methods=['POST'])
def call_test_parse_isodate():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    d = request_json.get("d")
    
    dt_fmt = request_json.get("dt_fmt")
    
    as_bytes = request_json.get("as_bytes")
    

    return test_parse_isodate(d, dt_fmt, as_bytes)

@app.route('/test_isodate_raises', methods=['POST'])
def call_test_isodate_raises():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isostr = request_json.get("isostr")
    
    exception = request_json.get("exception")
    

    return test_isodate_raises(isostr, exception)

@app.route('/test_parse_isodate_error_text', methods=['POST'])
def call_test_parse_isodate_error_text():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parse_isodate_error_text()

@app.route('/test_isotime', methods=['POST'])
def call_test_isotime():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    time_val = request_json.get("time_val")
    
    time_fmt = request_json.get("time_fmt")
    
    as_bytes = request_json.get("as_bytes")
    

    return test_isotime(time_val, time_fmt, as_bytes)

@app.route('/test_isotime_midnight', methods=['POST'])
def call_test_isotime_midnight():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isostr = request_json.get("isostr")
    

    return test_isotime_midnight(isostr)

@app.route('/test_isotime_raises', methods=['POST'])
def call_test_isotime_raises():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    isostr = request_json.get("isostr")
    
    exception = request_json.get("exception")
    

    return test_isotime_raises(isostr, exception)

@app.route('/test_YMD_could_be_day', methods=['POST'])
def call_test_YMD_could_be_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_YMD_could_be_day()

@app.route('/test_parser_private_warns', methods=['POST'])
def call_test_parser_private_warns():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parser_private_warns()

@app.route('/test_parser_parser_private_not_warns', methods=['POST'])
def call_test_parser_parser_private_not_warns():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_parser_parser_private_not_warns()

@app.route('/test_tzstr_internal_timedeltas', methods=['POST'])
def call_test_tzstr_internal_timedeltas():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_tzstr_internal_timedeltas()

@app.route('/test_timespec_auto', methods=['POST'])
def call_test_timespec_auto():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    dt = request_json.get("dt")
    
    sep = request_json.get("sep")
    

    return test_timespec_auto(dt, sep)

@app.route('/test_gettz_returns_local', methods=['POST'])
def call_test_gettz_returns_local():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    gettz_arg = request_json.get("gettz_arg")
    
    dt = request_json.get("dt")
    

    return test_gettz_returns_local(gettz_arg, dt)

@app.route('/test_convertyear', methods=['POST'])
def call_test_convertyear():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    n = request_json.get("n")
    

    return test_convertyear(n)

@app.route('/test_convertyear_no_specified_century', methods=['POST'])
def call_test_convertyear_no_specified_century():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    n = request_json.get("n")
    

    return test_convertyear_no_specified_century(n)

@app.route('/calculate_sha512', methods=['POST'])
def call_calculate_sha512():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    fpath = request_json.get("fpath")
    

    return calculate_sha512(fpath)

@app.route('/pointer_mock', methods=['POST'])
def call_pointer_mock():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return pointer_mock()

@app.route('/test_mlk_day', methods=['POST'])
def call_test_mlk_day():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return test_mlk_day()


if __name__ == "__main__":
    app.run(port=8080)