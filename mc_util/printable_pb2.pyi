"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import external_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PaymentRequest(google.protobuf.message.Message):
    """/ Message for a payment request, which combines a public address
    / with an a requested payment amount and memo field
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PUBLIC_ADDRESS_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    @property
    def public_address(self) -> external_pb2.PublicAddress:
        """/ The public address of the user requesting a payment"""
        pass
    value: builtins.int = ...
    """/ The requested value of the payment"""

    memo: typing.Text = ...
    """/ Any additional text explaining the request"""

    def __init__(self,
        *,
        public_address : typing.Optional[external_pb2.PublicAddress] = ...,
        value : builtins.int = ...,
        memo : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["public_address",b"public_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["memo",b"memo","public_address",b"public_address","value",b"value"]) -> None: ...
global___PaymentRequest = PaymentRequest

class TransferPayload(google.protobuf.message.Message):
    """/ Message encoding a private key and a UTXO, for the purpose of
    / giving someone access to an output. This would most likely be
    / used for gift cards.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ROOT_ENTROPY_FIELD_NUMBER: builtins.int
    TX_OUT_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    BIP39_ENTROPY_FIELD_NUMBER: builtins.int
    root_entropy: builtins.bytes = ...
    """/ [Deprecated] The root entropy, allowing the recipient to spend the money.
    / This has been replaced by a BIP39 entropy.
    """

    @property
    def tx_out_public_key(self) -> external_pb2.CompressedRistretto:
        """/ The public key of the UTXO to spend. This is an optimization, meaning
        / the recipient does not need to scan the entire ledger.
        """
        pass
    memo: typing.Text = ...
    """/ Any additional text explaining the gift"""

    bip39_entropy: builtins.bytes = ...
    """/ BIP39 entropy, allowing the recipient to spend the money.
    / When deriving an AccountKey from this entropy, account_index is always 0.
    """

    def __init__(self,
        *,
        root_entropy : builtins.bytes = ...,
        tx_out_public_key : typing.Optional[external_pb2.CompressedRistretto] = ...,
        memo : typing.Text = ...,
        bip39_entropy : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx_out_public_key",b"tx_out_public_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bip39_entropy",b"bip39_entropy","memo",b"memo","root_entropy",b"root_entropy","tx_out_public_key",b"tx_out_public_key"]) -> None: ...
global___TransferPayload = TransferPayload

class PrintableWrapper(google.protobuf.message.Message):
    """/ This wraps all of the above messages using "oneof", allowing us to
    / have a single encoding scheme and extend as necessary simply by adding
    / new messages without breaking backwards compatibility
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PUBLIC_ADDRESS_FIELD_NUMBER: builtins.int
    PAYMENT_REQUEST_FIELD_NUMBER: builtins.int
    TRANSFER_PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def public_address(self) -> external_pb2.PublicAddress: ...
    @property
    def payment_request(self) -> global___PaymentRequest: ...
    @property
    def transfer_payload(self) -> global___TransferPayload: ...
    def __init__(self,
        *,
        public_address : typing.Optional[external_pb2.PublicAddress] = ...,
        payment_request : typing.Optional[global___PaymentRequest] = ...,
        transfer_payload : typing.Optional[global___TransferPayload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["payment_request",b"payment_request","public_address",b"public_address","transfer_payload",b"transfer_payload","wrapper",b"wrapper"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["payment_request",b"payment_request","public_address",b"public_address","transfer_payload",b"transfer_payload","wrapper",b"wrapper"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["wrapper",b"wrapper"]) -> typing.Optional[typing_extensions.Literal["public_address","payment_request","transfer_payload"]]: ...
global___PrintableWrapper = PrintableWrapper