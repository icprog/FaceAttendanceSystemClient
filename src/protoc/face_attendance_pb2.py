# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: face_attendance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='face_attendance.proto',
  package='face_attendance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x66\x61\x63\x65_attendance.proto\x12\x0f\x66\x61\x63\x65_attendance\"G\n\x05Image\x12\x10\n\x08raw_data\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0c\n\x04high\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\"S\n\x04Info\x12\x10\n\x08staff_id\x18\x01 \x01(\x05\x12%\n\x05image\x18\x02 \x01(\x0b\x32\x16.face_attendance.Image\x12\x12\n\ntime_stamp\x18\x03 \x01(\t\"\"\n\x11\x44\x65tectFaceRequest\x12\r\n\x05state\x18\x01 \x01(\x05\"9\n\x12\x44\x65tectFaceResponse\x12#\n\x04info\x18\x01 \x03(\x0b\x32\x15.face_attendance.Info2g\n\nDetectFace\x12Y\n\x0c\x44oDetectFace\x12\".face_attendance.DetectFaceRequest\x1a#.face_attendance.DetectFaceResponse\"\x00\x62\x06proto3')
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='face_attendance.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_data', full_name='face_attendance.Image.raw_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='face_attendance.Image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='face_attendance.Image.high', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='face_attendance.Image.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=42,
  serialized_end=113,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='face_attendance.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='face_attendance.Info.staff_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='face_attendance.Info.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='face_attendance.Info.time_stamp', index=2,
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
  serialized_start=115,
  serialized_end=198,
)


_DETECTFACEREQUEST = _descriptor.Descriptor(
  name='DetectFaceRequest',
  full_name='face_attendance.DetectFaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='face_attendance.DetectFaceRequest.state', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=200,
  serialized_end=234,
)


_DETECTFACERESPONSE = _descriptor.Descriptor(
  name='DetectFaceResponse',
  full_name='face_attendance.DetectFaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='face_attendance.DetectFaceResponse.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=236,
  serialized_end=293,
)

_INFO.fields_by_name['image'].message_type = _IMAGE
_DETECTFACERESPONSE.fields_by_name['info'].message_type = _INFO
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['DetectFaceRequest'] = _DETECTFACEREQUEST
DESCRIPTOR.message_types_by_name['DetectFaceResponse'] = _DETECTFACERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'face_attendance_pb2'
  # @@protoc_insertion_point(class_scope:face_attendance.Image)
  ))
_sym_db.RegisterMessage(Image)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'face_attendance_pb2'
  # @@protoc_insertion_point(class_scope:face_attendance.Info)
  ))
_sym_db.RegisterMessage(Info)

DetectFaceRequest = _reflection.GeneratedProtocolMessageType('DetectFaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _DETECTFACEREQUEST,
  __module__ = 'face_attendance_pb2'
  # @@protoc_insertion_point(class_scope:face_attendance.DetectFaceRequest)
  ))
_sym_db.RegisterMessage(DetectFaceRequest)

DetectFaceResponse = _reflection.GeneratedProtocolMessageType('DetectFaceResponse', (_message.Message,), dict(
  DESCRIPTOR = _DETECTFACERESPONSE,
  __module__ = 'face_attendance_pb2'
  # @@protoc_insertion_point(class_scope:face_attendance.DetectFaceResponse)
  ))
_sym_db.RegisterMessage(DetectFaceResponse)



_DETECTFACE = _descriptor.ServiceDescriptor(
  name='DetectFace',
  full_name='face_attendance.DetectFace',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=295,
  serialized_end=398,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoDetectFace',
    full_name='face_attendance.DetectFace.DoDetectFace',
    index=0,
    containing_service=None,
    input_type=_DETECTFACEREQUEST,
    output_type=_DETECTFACERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTFACE)

DESCRIPTOR.services_by_name['DetectFace'] = _DETECTFACE

# @@protoc_insertion_point(module_scope)