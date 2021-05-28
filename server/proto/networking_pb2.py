# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='networking.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10networking.proto\"F\n\x14MsgSocketOpenRequest\x12\x0e\n\x06\x64omain\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\r\x12\x10\n\x08protocol\x18\x03 \x02(\r\"\'\n\x15MsgSocketOpenResponse\x12\x0e\n\x06handle\x18\x01 \x02(\x05\"K\n\nMsgRequest\x12\x32\n\x11socketOpenRequest\x18\x01 \x01(\x0b\x32\x15.MsgSocketOpenRequestH\x00\x42\t\n\x07payload\"N\n\x0bMsgResponse\x12\x34\n\x12socketOpenResponse\x18\x01 \x01(\x0b\x32\x16.MsgSocketOpenResponseH\x00\x42\t\n\x07payload'
)




_MSGSOCKETOPENREQUEST = _descriptor.Descriptor(
  name='MsgSocketOpenRequest',
  full_name='MsgSocketOpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='MsgSocketOpenRequest.domain', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='MsgSocketOpenRequest.type', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='MsgSocketOpenRequest.protocol', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=90,
)


_MSGSOCKETOPENRESPONSE = _descriptor.Descriptor(
  name='MsgSocketOpenResponse',
  full_name='MsgSocketOpenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='MsgSocketOpenResponse.handle', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=131,
)


_MSGREQUEST = _descriptor.Descriptor(
  name='MsgRequest',
  full_name='MsgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='socketOpenRequest', full_name='MsgRequest.socketOpenRequest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='MsgRequest.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=133,
  serialized_end=208,
)


_MSGRESPONSE = _descriptor.Descriptor(
  name='MsgResponse',
  full_name='MsgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='socketOpenResponse', full_name='MsgResponse.socketOpenResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='MsgResponse.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=210,
  serialized_end=288,
)

_MSGREQUEST.fields_by_name['socketOpenRequest'].message_type = _MSGSOCKETOPENREQUEST
_MSGREQUEST.oneofs_by_name['payload'].fields.append(
  _MSGREQUEST.fields_by_name['socketOpenRequest'])
_MSGREQUEST.fields_by_name['socketOpenRequest'].containing_oneof = _MSGREQUEST.oneofs_by_name['payload']
_MSGRESPONSE.fields_by_name['socketOpenResponse'].message_type = _MSGSOCKETOPENRESPONSE
_MSGRESPONSE.oneofs_by_name['payload'].fields.append(
  _MSGRESPONSE.fields_by_name['socketOpenResponse'])
_MSGRESPONSE.fields_by_name['socketOpenResponse'].containing_oneof = _MSGRESPONSE.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['MsgSocketOpenRequest'] = _MSGSOCKETOPENREQUEST
DESCRIPTOR.message_types_by_name['MsgSocketOpenResponse'] = _MSGSOCKETOPENRESPONSE
DESCRIPTOR.message_types_by_name['MsgRequest'] = _MSGREQUEST
DESCRIPTOR.message_types_by_name['MsgResponse'] = _MSGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSocketOpenRequest = _reflection.GeneratedProtocolMessageType('MsgSocketOpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGSOCKETOPENREQUEST,
  '__module__' : 'networking_pb2'
  # @@protoc_insertion_point(class_scope:MsgSocketOpenRequest)
  })
_sym_db.RegisterMessage(MsgSocketOpenRequest)

MsgSocketOpenResponse = _reflection.GeneratedProtocolMessageType('MsgSocketOpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSOCKETOPENRESPONSE,
  '__module__' : 'networking_pb2'
  # @@protoc_insertion_point(class_scope:MsgSocketOpenResponse)
  })
_sym_db.RegisterMessage(MsgSocketOpenResponse)

MsgRequest = _reflection.GeneratedProtocolMessageType('MsgRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUEST,
  '__module__' : 'networking_pb2'
  # @@protoc_insertion_point(class_scope:MsgRequest)
  })
_sym_db.RegisterMessage(MsgRequest)

MsgResponse = _reflection.GeneratedProtocolMessageType('MsgResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGRESPONSE,
  '__module__' : 'networking_pb2'
  # @@protoc_insertion_point(class_scope:MsgResponse)
  })
_sym_db.RegisterMessage(MsgResponse)


# @@protoc_insertion_point(module_scope)
