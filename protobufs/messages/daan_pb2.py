# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobufs/messages/daan.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobufs.messages import common_pb2 as protobufs_dot_messages_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobufs/messages/daan.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dprotobufs/messages/daan.proto\x1a\x1fprotobufs/messages/common.proto\"e\n\nPostfixMap\x12!\n\x03map\x18\x01 \x03(\x0b\x32\x14.PostfixMap.MapEntry\x1a\x34\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\x05value\x18\x02 \x01(\x0b\x32\x08.Strings:\x02\x38\x01\"[\n\x0bWikiChanges\x12\x16\n\x03\x61\x64\x64\x18\x01 \x03(\x0b\x32\t.WikiUser\x12\x0e\n\x06remove\x18\x02 \x03(\t\x12\x10\n\x08\x61\x63tivate\x18\x03 \x03(\t\x12\x12\n\ndeactivate\x18\x04 \x03(\t\":\n\x08WikiUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\thumanName\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"8\n\x0bLDAPChanges\x12\x19\n\x06upsert\x18\x01 \x03(\x0b\x32\t.LDAPUser\x12\x0e\n\x06remove\x18\x02 \x03(\t\"K\n\x08LDAPUser\x12\x0b\n\x03uid\x18\x01 \x01(\x0c\x12\r\n\x05\x65mail\x18\x02 \x01(\x0c\x12\x10\n\x08lastName\x18\x03 \x01(\x0c\x12\x11\n\thumanName\x18\x04 \x01(\x0c\"1\n\x0fLDAPNewPassword\x12\x0c\n\x04user\x18\x01 \x01(\x0c\x12\x10\n\x08password\x18\x02 \x01(\x0c\"?\n\x0e\x46otoadminEvent\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\thumanName\x18\x03 \x01(\t\"N\n\x13\x46otoadminMoveAction\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\r\n\x05store\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0b\n\x03\x64ir\x18\x04 \x01(\t\"\x19\n\x07Strings\x12\x0e\n\x06values\x18\x01 \x03(\t2\xd1\x02\n\x04\x44\x61\x61n\x12&\n\rSetPostfixMap\x12\x0b.PostfixMap\x1a\x06.Empty\"\x00\x12\x31\n\x18SetPostfixSenderLoginMap\x12\x0b.PostfixMap\x1a\x06.Empty\"\x00\x12*\n\x10\x41pplyWikiChanges\x12\x0c.WikiChanges\x1a\x06.Empty\"\x00\x12*\n\x10\x41pplyLDAPChanges\x12\x0c.LDAPChanges\x1a\x06.Empty\"\x00\x12-\n\x0fSetLDAPPassword\x12\x10.LDAPNewPassword\x1a\x06.Empty\"\x00\x12\x31\n\x14\x46otoadminCreateEvent\x12\x0f.FotoadminEvent\x1a\x06.Empty\"\x00\x12\x34\n\x12\x46otoadminMoveFotos\x12\x14.FotoadminMoveAction\x1a\x06.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[protobufs_dot_messages_dot_common__pb2.DESCRIPTOR,])




_POSTFIXMAP_MAPENTRY = _descriptor.Descriptor(
  name='MapEntry',
  full_name='PostfixMap.MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PostfixMap.MapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PostfixMap.MapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=167,
)

_POSTFIXMAP = _descriptor.Descriptor(
  name='PostfixMap',
  full_name='PostfixMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map', full_name='PostfixMap.map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POSTFIXMAP_MAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=167,
)


_WIKICHANGES = _descriptor.Descriptor(
  name='WikiChanges',
  full_name='WikiChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='add', full_name='WikiChanges.add', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='WikiChanges.remove', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activate', full_name='WikiChanges.activate', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deactivate', full_name='WikiChanges.deactivate', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=260,
)


_WIKIUSER = _descriptor.Descriptor(
  name='WikiUser',
  full_name='WikiUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='WikiUser.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humanName', full_name='WikiUser.humanName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='WikiUser.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=320,
)


_LDAPCHANGES = _descriptor.Descriptor(
  name='LDAPChanges',
  full_name='LDAPChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upsert', full_name='LDAPChanges.upsert', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='LDAPChanges.remove', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=378,
)


_LDAPUSER = _descriptor.Descriptor(
  name='LDAPUser',
  full_name='LDAPUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='LDAPUser.uid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='LDAPUser.email', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='LDAPUser.lastName', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humanName', full_name='LDAPUser.humanName', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=455,
)


_LDAPNEWPASSWORD = _descriptor.Descriptor(
  name='LDAPNewPassword',
  full_name='LDAPNewPassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='LDAPNewPassword.user', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='LDAPNewPassword.password', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=506,
)


_FOTOADMINEVENT = _descriptor.Descriptor(
  name='FotoadminEvent',
  full_name='FotoadminEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='FotoadminEvent.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='FotoadminEvent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humanName', full_name='FotoadminEvent.humanName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=571,
)


_FOTOADMINMOVEACTION = _descriptor.Descriptor(
  name='FotoadminMoveAction',
  full_name='FotoadminMoveAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='FotoadminMoveAction.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store', full_name='FotoadminMoveAction.store', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='FotoadminMoveAction.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dir', full_name='FotoadminMoveAction.dir', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=651,
)


_STRINGS = _descriptor.Descriptor(
  name='Strings',
  full_name='Strings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='Strings.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=678,
)

_POSTFIXMAP_MAPENTRY.fields_by_name['value'].message_type = _STRINGS
_POSTFIXMAP_MAPENTRY.containing_type = _POSTFIXMAP
_POSTFIXMAP.fields_by_name['map'].message_type = _POSTFIXMAP_MAPENTRY
_WIKICHANGES.fields_by_name['add'].message_type = _WIKIUSER
_LDAPCHANGES.fields_by_name['upsert'].message_type = _LDAPUSER
DESCRIPTOR.message_types_by_name['PostfixMap'] = _POSTFIXMAP
DESCRIPTOR.message_types_by_name['WikiChanges'] = _WIKICHANGES
DESCRIPTOR.message_types_by_name['WikiUser'] = _WIKIUSER
DESCRIPTOR.message_types_by_name['LDAPChanges'] = _LDAPCHANGES
DESCRIPTOR.message_types_by_name['LDAPUser'] = _LDAPUSER
DESCRIPTOR.message_types_by_name['LDAPNewPassword'] = _LDAPNEWPASSWORD
DESCRIPTOR.message_types_by_name['FotoadminEvent'] = _FOTOADMINEVENT
DESCRIPTOR.message_types_by_name['FotoadminMoveAction'] = _FOTOADMINMOVEACTION
DESCRIPTOR.message_types_by_name['Strings'] = _STRINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostfixMap = _reflection.GeneratedProtocolMessageType('PostfixMap', (_message.Message,), dict(

  MapEntry = _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), dict(
    DESCRIPTOR = _POSTFIXMAP_MAPENTRY,
    __module__ = 'protobufs.messages.daan_pb2'
    # @@protoc_insertion_point(class_scope:PostfixMap.MapEntry)
    ))
  ,
  DESCRIPTOR = _POSTFIXMAP,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:PostfixMap)
  ))
_sym_db.RegisterMessage(PostfixMap)
_sym_db.RegisterMessage(PostfixMap.MapEntry)

WikiChanges = _reflection.GeneratedProtocolMessageType('WikiChanges', (_message.Message,), dict(
  DESCRIPTOR = _WIKICHANGES,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:WikiChanges)
  ))
_sym_db.RegisterMessage(WikiChanges)

WikiUser = _reflection.GeneratedProtocolMessageType('WikiUser', (_message.Message,), dict(
  DESCRIPTOR = _WIKIUSER,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:WikiUser)
  ))
_sym_db.RegisterMessage(WikiUser)

LDAPChanges = _reflection.GeneratedProtocolMessageType('LDAPChanges', (_message.Message,), dict(
  DESCRIPTOR = _LDAPCHANGES,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:LDAPChanges)
  ))
_sym_db.RegisterMessage(LDAPChanges)

LDAPUser = _reflection.GeneratedProtocolMessageType('LDAPUser', (_message.Message,), dict(
  DESCRIPTOR = _LDAPUSER,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:LDAPUser)
  ))
_sym_db.RegisterMessage(LDAPUser)

LDAPNewPassword = _reflection.GeneratedProtocolMessageType('LDAPNewPassword', (_message.Message,), dict(
  DESCRIPTOR = _LDAPNEWPASSWORD,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:LDAPNewPassword)
  ))
_sym_db.RegisterMessage(LDAPNewPassword)

FotoadminEvent = _reflection.GeneratedProtocolMessageType('FotoadminEvent', (_message.Message,), dict(
  DESCRIPTOR = _FOTOADMINEVENT,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:FotoadminEvent)
  ))
_sym_db.RegisterMessage(FotoadminEvent)

FotoadminMoveAction = _reflection.GeneratedProtocolMessageType('FotoadminMoveAction', (_message.Message,), dict(
  DESCRIPTOR = _FOTOADMINMOVEACTION,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:FotoadminMoveAction)
  ))
_sym_db.RegisterMessage(FotoadminMoveAction)

Strings = _reflection.GeneratedProtocolMessageType('Strings', (_message.Message,), dict(
  DESCRIPTOR = _STRINGS,
  __module__ = 'protobufs.messages.daan_pb2'
  # @@protoc_insertion_point(class_scope:Strings)
  ))
_sym_db.RegisterMessage(Strings)


_POSTFIXMAP_MAPENTRY._options = None

_DAAN = _descriptor.ServiceDescriptor(
  name='Daan',
  full_name='Daan',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=681,
  serialized_end=1018,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetPostfixMap',
    full_name='Daan.SetPostfixMap',
    index=0,
    containing_service=None,
    input_type=_POSTFIXMAP,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetPostfixSenderLoginMap',
    full_name='Daan.SetPostfixSenderLoginMap',
    index=1,
    containing_service=None,
    input_type=_POSTFIXMAP,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyWikiChanges',
    full_name='Daan.ApplyWikiChanges',
    index=2,
    containing_service=None,
    input_type=_WIKICHANGES,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyLDAPChanges',
    full_name='Daan.ApplyLDAPChanges',
    index=3,
    containing_service=None,
    input_type=_LDAPCHANGES,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetLDAPPassword',
    full_name='Daan.SetLDAPPassword',
    index=4,
    containing_service=None,
    input_type=_LDAPNEWPASSWORD,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FotoadminCreateEvent',
    full_name='Daan.FotoadminCreateEvent',
    index=5,
    containing_service=None,
    input_type=_FOTOADMINEVENT,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FotoadminMoveFotos',
    full_name='Daan.FotoadminMoveFotos',
    index=6,
    containing_service=None,
    input_type=_FOTOADMINMOVEACTION,
    output_type=protobufs_dot_messages_dot_common__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAAN)

DESCRIPTOR.services_by_name['Daan'] = _DAAN

# @@protoc_insertion_point(module_scope)