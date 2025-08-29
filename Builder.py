#!/usr/bin/env python3
“””
Secure PyInstaller Builder for CTF Tools and Security Applications
Provides validated, error-handled executable building with security considerations.
“””

import os
import sys
import logging
from pathlib import Path
from typing import Optional, List
import PyInstaller.**main**

def validate_path(path: str, must_exist: bool = True) -> Path:
“””
Secure path validation with traversal protection.

```
@param {str} path - File or directory path to validate
@param {bool} must_exist - Whether path must exist (default: True)
@returns {Path} Validated Path object
@raises {ValueError} Invalid or potentially malicious path
@raises {FileNotFoundError} Required path doesn't exist
"""
try:
    # Convert to absolute path and resolve any symlinks/traversals
    validated_path = Path(path).resolve()
    
    # Security check: prevent directory traversal attacks
    if '..' in str(validated_path) or str(validated_path).startswith('/'):
        if not str(validated_path).startswith(str(Path.cwd())):
            raise ValueError(f"Path traversal detected: {path}")
    
    if must_exist and not validated_path.exists():
        raise FileNotFoundError(f"Required path not found: {validated_path}")
        
    return validated_path
    
except (OSError, ValueError) as e:
    raise ValueError(f"Invalid path '{path}': {e}")
```

def build_secure_executable(input_script: str,
output_dir: str = “dist”,
gui_mode: bool = True,
exclude_debug: bool = True) -> bool:
“””
Build executable with security-focused configuration.

```
@param {str} input_script - Path to main Python script
@param {str} output_dir - Output directory for executable  
@param {bool} gui_mode - Hide console window (default: True)
@param {bool} exclude_debug - Remove debug symbols (default: True)
@returns {bool} True if build successful, False otherwise
"""

# Configure logging for build process
logging.basicConfig(level=logging.INFO, 
                   format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

try:
    # Validate input paths with security checks
    script_path = validate_path(input_script, must_exist=True)
    output_path = validate_path(output_dir, must_exist=False)
    
    # Create output directory securely
    output_path.mkdir(parents=True, exist_ok=True, mode=0o755)
    
    # Build PyInstaller arguments with security considerations
    build_args = [
        str(script_path),                    # Input script (validated)
        '--onefile',                         # Single executable file
        '--clean',                          # Clean build cache
        '--distpath', str(output_path),     # Secure output path
        '-p', str(script_path.parent),      # Python path for imports
    ]
    
    # GUI/Console mode configuration
    if gui_mode:
        build_args.append('--windowed')     # Hide console (GUI apps)
    else:
        build_args.append('--console')      # Show console (CLI tools)
    
    # Security hardening options
    if exclude_debug:
        build_args.extend([
            '--strip',                      # Remove debug symbols (Linux/Mac)
            '--exclude-module', 'pdb',      # Remove Python debugger
            '--exclude-module', 'pydoc',    # Remove documentation
        ])
    
    # Additional security exclusions for CTF/security tools
    security_exclusions = [
        'tkinter',      # GUI framework (reduce size)
        'matplotlib',   # Plotting library (large)  
        'PIL',         # Image processing
        'unittest',    # Testing framework
    ]
    
    for module in security_exclusions:
        build_args.extend(['--exclude-module', module])
    
    logger.info(f"Building: {script_path.name}")
    logger.info(f"Output: {output_path}")
    logger.info(f"Mode: {'GUI' if gui_mode else 'Console'}")
    
    # Execute PyInstaller with error handling
    PyInstaller.__main__.run(build_args)
    
    # Verify build output exists
    expected_exe = output_path / f"{script_path.stem}.exe"
    if expected_exe.exists():
        logger.info(f"✓ Build successful: {expected_exe}")
        logger.info(f"✓ Size: {expected_exe.stat().st_size:,} bytes")
        return True
    else:
        logger.error("✗ Build completed but executable not found")
        return False
        
except (ValueError, FileNotFoundError) as e:
    logger.error(f"✗ Validation error: {e}")
    return False
except KeyboardInterrupt:
    logger.warning("✗ Build cancelled by user")
    return False
except Exception as e:
    logger.error(f"✗ Build failed: {e}")
    return False
```

def build_ctf_tool(script_path: str, tool_name: Optional[str] = None) -> bool:
“””
Optimized build configuration for CTF and security tools.

```
@param {str} script_path - Path to CTF tool script
@param {str} tool_name - Optional custom name for executable
@returns {bool} Build success status
"""

try:
    validated_script = validate_path(script_path)
    output_name = tool_name or f"ctf_{validated_script.stem}"
    
    # CTF tools typically need console output
    success = build_secure_executable(
        input_script=script_path,
        output_dir="tools",  # Separate directory for CTF tools
        gui_mode=False,      # Console mode for output/interaction
        exclude_debug=True   # Reduce file size and remove debug info
    )
    
    if success:
        logging.info(f"✓ CTF tool ready: tools/{output_name}")
        
    return success
    
except Exception as e:
    logging.error(f"✗ CTF build failed: {e}")
    return False
```

# Example usage with fallback error handling

def main():
“””
Main execution with comprehensive error handling and examples.
Demonstrates secure build patterns for different use cases.
“””

```
try:
    # Example 1: Standard GUI application build
    if build_secure_executable("Main.py"):
        print("✓ GUI application built successfully")
    
    # Example 2: CTF/Security tool build  
    # build_ctf_tool("exploit.py", "network_scanner")
    
    # Example 3: Console application with custom settings
    # build_secure_executable("cli_tool.py", "bin", gui_mode=False)
    
except KeyboardInterrupt:
    print("\n✗ Build process interrupted")
    sys.exit(1)
except Exception as e:
    print(f"✗ Critical error: {e}")
    sys.exit(1)
```

if **name** == “**main**”:
main()
