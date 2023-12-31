# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18spacemesh/v1/types.proto\x12\x0cspacemesh.v1\"\x1a\n\tSimpleInt\x12\r\n\x05value\x18\x01 \x01(\x04\"\x1d\n\x0cSimpleString\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06\x41mount\x12\r\n\x05value\x18\x01 \x01(\x04\"\x1c\n\tAccountId\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x1b\n\rTransactionId\x12\n\n\x02id\x18\x01 \x01(\x0c\"\x1a\n\x0c\x41\x63tivationId\x12\n\n\x02id\x18\x01 \x01(\x0c\"\x17\n\tSmesherId\x12\n\n\x02id\x18\x01 \x01(\x0c\"\x89\x02\n\nActivation\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.spacemesh.v1.ActivationId\x12(\n\x05layer\x18\x02 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12+\n\nsmesher_id\x18\x03 \x01(\x0b\x32\x17.spacemesh.v1.SmesherId\x12)\n\x08\x63oinbase\x18\x04 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12,\n\x08prev_atx\x18\x05 \x01(\x0b\x32\x1a.spacemesh.v1.ActivationId\x12\x11\n\tnum_units\x18\x06 \x01(\r\x12\x10\n\x08sequence\x18\x07 \x01(\x04\"\x93\x02\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\x0c\x12*\n\tprincipal\x18\x02 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12)\n\x08template\x18\x03 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12\x0e\n\x06method\x18\x04 \x01(\r\x12\"\n\x05nonce\x18\x05 \x01(\x0b\x32\x13.spacemesh.v1.Nonce\x12)\n\x06limits\x18\x06 \x01(\x0b\x32\x19.spacemesh.v1.LayerLimits\x12\x0f\n\x07max_gas\x18\x07 \x01(\x04\x12\x11\n\tgas_price\x18\x08 \x01(\x04\x12\x11\n\tmax_spend\x18\t \x01(\x04\x12\x0b\n\x03raw\x18\n \x01(\x0c\"\'\n\x0bLayerLimits\x12\x0b\n\x03min\x18\x01 \x01(\r\x12\x0b\n\x03max\x18\x02 \x01(\r\"*\n\x05Nonce\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x04\x12\x10\n\x08\x62itfield\x18\x02 \x01(\r\"n\n\x0fMeshTransaction\x12.\n\x0btransaction\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.Transaction\x12+\n\x08layer_id\x18\x02 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\"\x8b\x02\n\x06Reward\x12(\n\x05layer\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12#\n\x05total\x18\x02 \x01(\x0b\x32\x14.spacemesh.v1.Amount\x12*\n\x0clayer_reward\x18\x03 \x01(\x0b\x32\x14.spacemesh.v1.Amount\x12\x31\n\x0elayer_computed\x18\x04 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12)\n\x08\x63oinbase\x18\x05 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12(\n\x07smesher\x18\x06 \x01(\x0b\x32\x17.spacemesh.v1.SmesherId\"\xa4\x01\n\x05\x42lock\x12\n\n\x02id\x18\x01 \x01(\x0c\x12/\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x19.spacemesh.v1.Transaction\x12\x31\n\ractivation_id\x18\x03 \x01(\x0b\x32\x1a.spacemesh.v1.ActivationId\x12+\n\nsmesher_id\x18\x04 \x01(\x0b\x32\x17.spacemesh.v1.SmesherId\"\xdc\x02\n\x05Layer\x12)\n\x06number\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.spacemesh.v1.Layer.LayerStatus\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\x12#\n\x06\x62locks\x18\x04 \x03(\x0b\x32\x13.spacemesh.v1.Block\x12-\n\x0b\x61\x63tivations\x18\x05 \x03(\x0b\x32\x18.spacemesh.v1.Activation\x12\x17\n\x0froot_state_hash\x18\x06 \x01(\x0c\"|\n\x0bLayerStatus\x12\x1c\n\x18LAYER_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15LAYER_STATUS_APPROVED\x10\x01\x12\x1a\n\x16LAYER_STATUS_CONFIRMED\x10\x02\x12\x18\n\x14LAYER_STATUS_APPLIED\x10\x03\"\x1d\n\x0bLayerNumber\x12\x0e\n\x06number\x18\x01 \x01(\r\"\x1d\n\x0b\x45pochNumber\x12\x0e\n\x06number\x18\x01 \x01(\r\"P\n\x08\x41ppEvent\x12\x33\n\x0etransaction_id\x18\x01 \x01(\x0b\x32\x1b.spacemesh.v1.TransactionId\x12\x0f\n\x07message\x18\x02 \x01(\tB4Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_SIMPLEINT']._serialized_start=42
  _globals['_SIMPLEINT']._serialized_end=68
  _globals['_SIMPLESTRING']._serialized_start=70
  _globals['_SIMPLESTRING']._serialized_end=99
  _globals['_AMOUNT']._serialized_start=101
  _globals['_AMOUNT']._serialized_end=124
  _globals['_ACCOUNTID']._serialized_start=126
  _globals['_ACCOUNTID']._serialized_end=154
  _globals['_TRANSACTIONID']._serialized_start=156
  _globals['_TRANSACTIONID']._serialized_end=183
  _globals['_ACTIVATIONID']._serialized_start=185
  _globals['_ACTIVATIONID']._serialized_end=211
  _globals['_SMESHERID']._serialized_start=213
  _globals['_SMESHERID']._serialized_end=236
  _globals['_ACTIVATION']._serialized_start=239
  _globals['_ACTIVATION']._serialized_end=504
  _globals['_TRANSACTION']._serialized_start=507
  _globals['_TRANSACTION']._serialized_end=782
  _globals['_LAYERLIMITS']._serialized_start=784
  _globals['_LAYERLIMITS']._serialized_end=823
  _globals['_NONCE']._serialized_start=825
  _globals['_NONCE']._serialized_end=867
  _globals['_MESHTRANSACTION']._serialized_start=869
  _globals['_MESHTRANSACTION']._serialized_end=979
  _globals['_REWARD']._serialized_start=982
  _globals['_REWARD']._serialized_end=1249
  _globals['_BLOCK']._serialized_start=1252
  _globals['_BLOCK']._serialized_end=1416
  _globals['_LAYER']._serialized_start=1419
  _globals['_LAYER']._serialized_end=1767
  _globals['_LAYER_LAYERSTATUS']._serialized_start=1643
  _globals['_LAYER_LAYERSTATUS']._serialized_end=1767
  _globals['_LAYERNUMBER']._serialized_start=1769
  _globals['_LAYERNUMBER']._serialized_end=1798
  _globals['_EPOCHNUMBER']._serialized_start=1800
  _globals['_EPOCHNUMBER']._serialized_end=1829
  _globals['_APPEVENT']._serialized_start=1831
  _globals['_APPEVENT']._serialized_end=1911
# @@protoc_insertion_point(module_scope)
