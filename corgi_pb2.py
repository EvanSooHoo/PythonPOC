# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corgi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63orgi.proto\x12\x0fpackageOfCorgis\"!\n\x0c\x43orgiRequest\x12\x11\n\tcorgindex\x18\x01 \x01(\t\"\x1c\n\tWoofReply\x12\x0f\n\x07message\x18\x01 \x01(\t2R\n\x08RpcCorgi\x12\x46\n\x07SayWoof\x12\x1d.packageOfCorgis.CorgiRequest\x1a\x1a.packageOfCorgis.WoofReply\"\x00\x62\x06proto3')



_CORGIREQUEST = DESCRIPTOR.message_types_by_name['CorgiRequest']
_WOOFREPLY = DESCRIPTOR.message_types_by_name['WoofReply']
CorgiRequest = _reflection.GeneratedProtocolMessageType('CorgiRequest', (_message.Message,), {
  'DESCRIPTOR' : _CORGIREQUEST,
  '__module__' : 'corgi_pb2'
  # @@protoc_insertion_point(class_scope:packageOfCorgis.CorgiRequest)
  })
_sym_db.RegisterMessage(CorgiRequest)

WoofReply = _reflection.GeneratedProtocolMessageType('WoofReply', (_message.Message,), {
  'DESCRIPTOR' : _WOOFREPLY,
  '__module__' : 'corgi_pb2'
  # @@protoc_insertion_point(class_scope:packageOfCorgis.WoofReply)
  })
_sym_db.RegisterMessage(WoofReply)

_RPCCORGI = DESCRIPTOR.services_by_name['RpcCorgi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CORGIREQUEST._serialized_start=32
  _CORGIREQUEST._serialized_end=65
  _WOOFREPLY._serialized_start=67
  _WOOFREPLY._serialized_end=95
  _RPCCORGI._serialized_start=97
  _RPCCORGI._serialized_end=179
# @@protoc_insertion_point(module_scope)
