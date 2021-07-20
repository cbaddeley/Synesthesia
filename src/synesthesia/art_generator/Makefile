RUSTC = rustc
RUST_FLAGS = --crate-type=dylib

SOURCE_FILES = rusty.rs
OUTPUT_FILE = rusty.so

libxorcipher.so: ${SOURCE_FILES}
	${RUSTC} ${RUST_FLAGS} -o ${OUTPUT_FILE} ${SOURCE_FILES}

clean:
	rm ${OUTPUT_FILE}
