from formatting import FormatType


"""
opcode = unique instruction code
format_type = determine how to read in bits
operation = list of format values to fill
assembly = <instruction> assembly (ie. how the actual assembly looks like)
"""
instruct_dir = {
    "ADD":
    {
        "opcode": b'10001011000',  # ADD
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn + Rm
        "assembly": "XRd, XRn, XRm",
    },
    "ADDI": {
        "opcode": b'1001000100',  # ADD Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn + ALUImm
        "assembly": "XRd, XRn, aluimm",
    },
    "AND": {
        "opcode": b'10001010000',  # AND
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn & Rm
        "assembly": "",  # TODO
    },
    "ANDI": {
        "opcode": b'1001001000',  # AND Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn & ALUImm
        "assembly": "",  # TODO
    },
    "B": {
        "opcode": b'000101',  # Branch
        "format_type": FormatType.B,
        "operation": ["braddr"],  # PC = PC + BranchAddr
        "assembly": "braddr",
    },
    "B.cond": {
        "opcode": b'01010100',  # Branch Conditionally
        "format_type": FormatType.CB,
        "operation": ["condaddr"],  # if (FLAGS == cond) -> PC = PC + CondBranchAddr
        "assembly": "condaddr",
    },
    "BL": {
        "opcode": b'100101',  # Branch with Link
        "format_type": FormatType.B,
        "operation": ["braddr"],  # R[30] = PC + 4; PC = PC + BranchAddr
        "assembly": "braddr",
    },
    "BR": {
        "opcode": b'11010110000',  # Branch to Register
        "format_type": FormatType.R,
        "operation": ["Rt"],  # PC = Rt
        "assembly": "Rt",
    },
    "CBNZ": {
        "opcode": b'10110101',  # Compare & Branch if Not Zero
        "format_type": FormatType.CB,
        "operation": ["Rt", "condaddr"],  # if(Rt != 0) -> PC = PC + CondBranchAddr
    },
    "CBZ": {
        "opcode": b'10110100',  # Compare & Branch if Zero
        "format_type": FormatType.CB,
        "operation": ["condaddr"],  # if (Rt == 0) -> PC = PC + CondBranchAddr
        "assembly": "",  # TODO
    },
    "DUMP": {
        "opcode": b'11111111110',  # TODO
        "format_type": FormatType.R,
        "operation": [],  # TODO
        "assembly": "", # TODO
    },
    "EOR": {
        "opcode": b'11001010000',  # Exclusive OR
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn ^ Rm
        "assembly": "",  # TODO
    },
    "EORI": {
        "opcode": b'1101001000',  # Exclusive OR Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn ^ ALUImm
        "assembly": "",  # TODO
    },
    "HALT": {
        "opcode": b'11111111111',  # TODO
        "format_type": FormatType.R,
        "operation": [],  # TODO
        "assebly": "",  # TODO
    },
    "LDUR": {
        "opcode": b'11111000010',  # Load Register Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = [Rn + DTAddr]
        "assembly": "Rt, [Rn, dtaddr]",
    },
    "LDURB": {
        "opcode": b'00111000010',  # Load Byte Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = {56'b0, [Rn + DTAddr](7:0)}
        "assembly": "",  # TODO
    },
    "LDURH": {
        "opcode": b'01111000010',  # Load Half Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = {48'b0, [Rn + DTAddr](15:0)}
        "assembly": "",  # TODO
    },
    "LDURSW": {
        "opcode": b'10111000100',  # Load Signed Word Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = {32{[Rn + DTAddr][31]}, [Rn + DTAddr](31:0)}
        "assembly": "",  # TODO
    },
    "LSL": {
        "opcode": b"11010011011",  # Logical Shift Left
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "shamt"],  # Rd = Rn << shamt
        "assembly": "Rd, Rn, #shamt",
    },
    "LSR": {
        "opcode": b"11010011010",  # Logical Shift Right
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "shamt"],  # Rd = Rn >>> shamt
        "assembly": "Rd, Rn, #shamt",
    },
    "MUL": {
        "opcode": b"10011011000",  # Multiply
        "format_type": FormatType.R,
        "shamt": b"011111",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)(63:0)
        "assembly": "",  # TODO
    },
    "ORR": {
        "opcode": b"10101010000",  # Inclusive OR
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn | Rm
        "assembly": "",  # TODO
    },
    "ORRI": {
        "opcode": b"1011001000",  # Inclusive OR Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluim"],  # Rd = Rn | ALUImm
        "assembly": "",  # TODO
    },
    "PRNL": {
        "opcode": b"11111111100",  # TODO
        "format_type": FormatType.R,
        "operation": [],  # TODO
        "assembly": "",  # TODO
    },
    "PRNT": {
        "opcode": b"11111111101",  # TODO
        "format_type": FormatType.R,
        "operation": [],  # TODO
        "assembly": "",  # TODO
    },
    "SDIV": {
        "opcode": b"10011010110",  # Signed Divide
        "format_type": FormatType.R,
        "shamt": b"000010",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn / Rm
        "assembly": "",  # TODO
    },
    "SMULH": {
        "opcode": b"10011011010",  # Signed Multiply High
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)(127:64)
        "assembly": "",  # TODO
    },
    "STUR": {
        "opcode": b"11111000000",  # Store Register Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rn", "dtaddr", "Rt"],  # [Rn + DTAddr] = Rt
        "assembly": "Rt, [Rn, dtaddr]",
    },
    "STURW": {
        "opcode": b"10111000000",  # Store Word Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rn", "dtaddr", "Rt"],  # [Rn + DTAddr](31:0) = Rt(31:0)
        "assembly": "",  # TODO

    },
    "SUB": {
        "opcode": b"11001011000",  # Subtract
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn - Rm
        "assembly": "Rd, Rn, Rm",
    },
    "SUBI": {
        "opcode": b"1101000100",  # Subtract Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluim"],  # Rd = Rn - ALUImm
        "assembly": "Rd, Rn, aluim",
    },
    "SUBIS": {
        "opcode": b"1111000100",  # Subtract Immediate & Set Flags
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluim"],  # Rd, FLAGS = Rn - ALUImm
        "assembly": "",  # TODO
    },
    "SUBS": {
        "opcode": b"11101011000",  # Subtract & Set Flags
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd, FLAGS = Rn - Rm
        "assembly": "",  # TODO
    },
    "UDIV": {
        "opcode": b"10011010110",  # Unsigned Divide
        "format_type": FormatType.R,
        "shamt": b"000011",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn / Rm
        "assembly": "",  # TODO
    },
    "UMULH": {
        "opcode": b"10011011110",  # Unsigned Multiply High
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)(127:64)
        "assembly": "",  # TODO
    },
}

# B.cond condition extensions
conditions = {
    "EQ": 0x0,
    "NE": 0x1,
    "HS": 0x2,
    "LO": 0x3,
    "MI": 0x4,
    "PL": 0x5,
    "VS": 0x6,
    "VC": 0x7,
    "HI": 0x8,
    "LS": 0x9,
    "GE": 0x10,
    "LT": 0x11,
    "GT": 0x12,
    "LE": 0x13,
}